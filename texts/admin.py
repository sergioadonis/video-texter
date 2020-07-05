from django.contrib import admin
from .models import YoutubeVideo, YoutubeVideoTask
from .tasks import import_youtubevideo_data, update_youtubevideo_data


@admin.register(YoutubeVideo)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'language_code')
    actions = ['import_data']

    def import_data(self, request, queryset):
        tasks = []
        for obj in queryset:
            url = obj.url
            pk = obj.pk
            task_id = import_youtubevideo_data.apply_async(args=(url,), link=update_youtubevideo_data.s(pk))
            task = YoutubeVideoTask(youtubevideo=obj, task_id=task_id) 
            tasks.append(task)
        YoutubeVideoTask.objects.bulk_create(tasks)

    import_data.short_description = 'Import data from Youtube'

