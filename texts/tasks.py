# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import task
from . import models


@task
def update_youtube_link_info(pk):
    print('Staring update_youtube_link_info task - pk: {0}'.format(pk))
    instance = models.YoutubeLink.objects.get(pk=pk)
    if instance.must_update_title_or_language_code():
        pass
