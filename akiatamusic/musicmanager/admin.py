from django.contrib import admin

from musicmanager.models import Song

class SongAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'title', 'album', 'source', 'create_date', 'modified_date')
    list_filter = ('source',)
    #ordering = ('-id',)
admin.site.register(Song, SongAdmin)
