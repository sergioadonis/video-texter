from django.contrib import admin
from .models import YoutubeVideo 
from .tasks import import_youtubevideo_data, copy_youtubevideo_tos3


@admin.register(YoutubeVideo)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'language_code')
    actions = ['import_data', 'copy_tos3']

    def import_data(self, request, queryset):
        for obj in queryset:
            url = obj.url
            pk = obj.pk
            import_youtubevideo_data.delay(pk=pk, url=url)
    import_data.short_description = 'Import data from Youtube'

    def copy_tos3(self, request, queryset):
        for obj in queryset:
            url = obj.url
            pk = obj.pk
            copy_youtubevideo_tos3.delay(pk=pk, url=url, bucket='sa-video-samples')
    copy_tos3.short_description = 'Copy video from Youtube to S3'



