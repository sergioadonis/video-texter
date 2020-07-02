from django.contrib import admin
from . import models


@admin.register(models.YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('link',)
