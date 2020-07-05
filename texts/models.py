from django.db import models
from django.contrib.postgres.fields import JSONField


class YoutubeVideo(models.Model):
    url = models.CharField(max_length=50)
    task_id = models.CharField(max_length=255, blank=True, default='')
    data = JSONField(default=dict, blank=True)

    def __str__(self):
        return self.title if self.title else self.url

    @property
    def title(self):
        try:
            return self.data['snippet']['title']
        except:
            return ''

    @property
    def language_code(self):
        try:
            return self.data['snippet']['defaultAudioLanguage']
        except:
            return ''
