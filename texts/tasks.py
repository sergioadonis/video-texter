# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task
from youtube_dl import YoutubeDL
import boto3
from botocore.config import Config
from .models import YoutubeVideo


@task
def import_youtubevideo_data(pk, url):
    print('Starting import_youtubevideo_data task - pk: {0}; url: {1}'.format(pk, url))

    options = {
        'skip_download': True
    } 
    ydl = YoutubeDL(options)
    result = ydl.extract_info(url=url)
    if 'formats' in result:
        del result['formats']
    YoutubeVideo.objects.filter(pk=pk).update(data=result)

    print('End import_youtubevideo_data task - pk: {0}; url: {1}'.format(pk, url))    
    return result


@task
def copy_youtubevideo_tos3(pk, url, bucket):
    print('Starting copy_youtubevideo_tos3 task - pk: {0}; url: {1}'.format(pk, url))

    name = '{0}.mp3'.format(pk)
    filename = '/tmp/videos/{0}'.format(name)
    options = {
        'outtmpl': filename,
        'format': 'bestaudio'
    }    
    ydl = YoutubeDL(options)
    ydl_result = ydl.download([url])

    print('Starting upload to Amazon S3...')
    s3 = boto3.resource('s3')
    s3_result = s3.Object(bucket, name).upload_file(filename)
    
    print('End copy_youtubevideo_tos3 task - pk: {0}; url: {1}'.format(pk, url))
    return {
        'locals': {
            'pk': pk,
            'url': url,
            'filename': filename,
            'bucket': bucket,
            'name': name,
            'ydl_result': ydl_result,
            's3_result': s3_result
        }
    }
