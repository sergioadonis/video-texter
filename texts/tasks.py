# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task


@task
def import_youtubevideo_data(pk, url):
    print('Starting import_youtubevideo_data task - pk: {0}; url: {1}'.format(pk, url))

    mock_data = {
        'pk': pk,
        'url': url,
        'snippet': {
            'title': 'Other Title to Testing',
            'defaultAudioLanguage': 'en-US'
        }
    }

    from .models import YoutubeVideo
    YoutubeVideo.objects.filter(pk=pk).update(data=mock_data)
    
    return mock_data

