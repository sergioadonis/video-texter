# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task


@task
def import_youtubelink_data(url):
    print('Starting import_youtubelink_data task - url: {0}'.format(url))
    mock_data = {
        'snippet': {
            'title': 'Other Title to Testing',
            'defaultAudioLanguage': 'en-US'
        }
    }
    return mock_data


@task
def update_youtubelink_data(result, youtubelink_pk):
    print('Starting update_youtubelink_data - youtubelink_pk: {0}'.format(youtubelink_pk))
    from .models import YoutubeLink
    YoutubeLink.objects.filter(pk=youtubelink_pk).update(data=result)

