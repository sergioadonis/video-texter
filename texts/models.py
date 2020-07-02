from django.db import models


class YoutubeLink(models.Model):
    link = models.CharField(max_length=50)
    title = models.CharField(max_length=50, default='', blank=True)
    language_code = models.CharField(max_length=5, default='', blank=True)

    def __str__(self):
        return self.title if self.title else self.link
