from django.contrib import admin
from .models import YoutubeLink
from .tasks import refresh_youtubelink_data


@admin.register(YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'title', 'language_code')
    actions = ['refresh_data']

    def refresh_data(self, request, queryset):
        for obj in queryset:
            refresh_youtubelink_data.delay(obj.pk)
    refresh_data.short_description = 'Refresh data'

