from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models
from . import tasks


@receiver(post_save, sender=models.YoutubeLink)
def youtube_link_post_save(sender, **kwargs):
    instance = kwargs['instance']
    if instance.must_update_title_or_language_code():
        tasks.update_youtube_link_info.delay(instance.pk)