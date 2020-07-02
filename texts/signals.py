from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YoutubeLink
from .tasks import update_youtube_link_info


@receiver(post_save, sender=YoutubeLink)
def youtube_link_post_save(sender, **kwargs):
    instance = kwargs['instance']
    if instance.must_update_title_or_language_code():
        update_youtube_link_info.delay(instance.pk)