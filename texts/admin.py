from django.contrib import admin
from .models import YoutubeVideo
from .tasks import import_youtubevideo_data, update_youtubevideo_data


@admin.register(YoutubeVideo)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'language_code', 'task_id')
    actions = ['import_data']

    def import_data(self, request, queryset):
        for obj in queryset:
            url = obj.url
            pk = obj.pk
            task_id = import_youtubevideo_data.apply_async(args=(url,), link=update_youtubevideo_data.s(pk))
            obj.task_id = task_id
        YoutubeVideo.objects.bulk_update(list(queryset), ['task_id'])

    import_data.short_description = 'Import data from Youtube'

