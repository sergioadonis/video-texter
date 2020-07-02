# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task
from .models import YoutubeLink


@task
def refresh_youtubelink_data(pk):
    print('Staring refresh_youtubelink_data task - pk: {0}'.format(pk))
    instance = YoutubeLink.objects.get(pk=pk)
    link = instance.link
    print(link)

