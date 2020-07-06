from django.contrib import admin
from .models import YoutubeVideo 
from .tasks import import_youtubevideo_data #, update_youtubevideo_data


@admin.register(YoutubeVideo)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'language_code')
    actions = ['import_data']

    def import_data(self, request, queryset):
        for obj in queryset:
            url = obj.url
            pk = obj.pk
            # import_youtubevideo_data.apply_async(args=(url,), link=update_youtubevideo_data.s(pk))
            import_youtubevideo_data.delay(pk=pk, url=url)

    import_data.short_description = 'Import data from Youtube'

