from django.db import models
from django.contrib.postgres.fields import JSONField


class YoutubeVideo(models.Model):
    url = models.CharField(max_length=50)
    data = JSONField(default=dict, blank=True)
    s3_url = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.title if self.title else self.url

    @property
    def video_id(self):
        try:
            return self.url[-11:]
        except:
            return ''

    @property
    def title(self):
        try:
            return self.data['title']
        except:
            return ''

    @property
    def language_code(self):
        try:
            return self.data['snippet']['defaultAudioLanguage']
        except:
            return ''

