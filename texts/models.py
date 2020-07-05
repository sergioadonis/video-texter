from django.db import models
from django.contrib.postgres.fields import JSONField


class YoutubeLink(models.Model):
    link = models.CharField(max_length=50)
    task_id = models.CharField(max_length=255, blank=True, default='')
    data = JSONField(default=dict, blank=True)

    def __str__(self):
        return self.title if self.title else self.link

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
