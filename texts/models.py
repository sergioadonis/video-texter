from django.db import models


class YoutubeLink(models.Model):
    link = models.CharField(max_length=50)
