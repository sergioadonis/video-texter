# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task
from .models import YoutubeLink


@task
def update_youtube_link_info(pk):
    print('Staring update_youtube_link_info task - pk: {0}'.format(pk))
    instance = YoutubeLink.objects.get(pk=pk)
    if instance.must_update_title_or_language_code():
        pass
