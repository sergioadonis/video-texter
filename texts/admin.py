from django.contrib import admin
from .models import YoutubeLink
from .tasks import import_youtubelink_data


@admin.register(YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'title', 'language_code', 'task_id')
    actions = ['import_data']

    def import_data(self, request, queryset):
        for obj in queryset:
            url = obj.link
            task_id = import_youtubelink_data.apply_async(args=(url,))
            obj.task_id = task_id
        YoutubeLink.objects.bulk_update(list(queryset), ['task_id'])

    import_data.short_description = 'Import data from Youtube'

