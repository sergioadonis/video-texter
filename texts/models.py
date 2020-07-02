from django.db import models
from django.contrib.postgres.fields import JSONField


class YoutubeLink(models.Model):
    link = models.CharField(max_length=50)
    data = JSONField(default=dict, blank=True)
#    title = models.CharField(max_length=50, default='', blank=True)
#    language_code = models.CharField(max_length=5, default='', blank=True)

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

    def must_update_title_or_language_code(self):
        if len(self.link) == 0:
            return False
        if len(self.language_code) == 0 or len(self.title) == 0:
            return True
