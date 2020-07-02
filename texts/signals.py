from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.YoutubeLink)
def youtube_link_post_save(sender, **kwargs):
    pass