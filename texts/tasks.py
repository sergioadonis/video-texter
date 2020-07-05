# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task


@task
def import_youtubelink_data(url):
    print('Starting import_youtubelink_data task - url: {0}'.format(url))
    mock_data = {
        'url': url,
        'response': {
            'snippet': {
                'title': 'Other Title to Testing',
                'defaultAudioLanguage': 'en-US'
            }
        }
    }
    return mock_data


@task
def update_youtubelink_data(task_id, result):
    print('Starting update_youtubelink_data - task_id: {0}'.format(task_id))
    import json
    response = json.loads(result)['response']
    from .models import YoutubeLink
    YoutubeLink.objects.filter(task_id=task_id).update(data=response)

