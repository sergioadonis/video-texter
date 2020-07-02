from django.contrib import admin
from .models import YoutubeLink


@admin.register(YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'title', 'language_code')
