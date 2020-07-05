from django.contrib import admin
from .models import YoutubeLink
from .tasks import import_youtubelink_data, update_youtubelink_data


@admin.register(YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'title', 'language_code', 'task_id')
    actions = ['import_data']

    def import_data(self, request, queryset):
        for obj in queryset:
            url = obj.link
            pk = obj.pk
            task_id = import_youtubelink_data.apply_async(args=(url,), link=update_youtubelink_data.s(pk))
            obj.task_id = task_id
        YoutubeLink.objects.bulk_update(list(queryset), ['task_id'])

    import_data.short_description = 'Import data from Youtube'

