from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_results.models import TaskResult
from celery import states
from .tasks import update_youtubelink_data, import_youtubelink_data


@receiver(post_save, sender=TaskResult)
def taskresult_post_save(sender, instance, **kwargs):
    if instance.status == states.SUCCESS:
        if instance.task_name.endswith(import_youtubelink_data.__name__):
            task_id = instance.task_id
            result = instance.result
            update_youtubelink_data.apply_async(args=(task_id, result,))

