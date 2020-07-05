# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task


@task
def import_youtubevideo_data(url):
    print('Starting import_youtubevideo_data task - url: {0}'.format(url))
    mock_data = {
        'snippet': {
            'title': 'Other Title to Testing',
            'defaultAudioLanguage': 'en-US'
        }
    }
    return mock_data


@task
def update_youtubevideo_data(result, pk):
    print('Starting update_youtubevideo_data - pk: {0}; result: {1}'.format(pk, result))
    from .models import YoutubeVideo
    YoutubeVideo.objects.filter(pk=pk).update(data=result)

