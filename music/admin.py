from .models import Song, Album, Performer
from django.contrib import admin


@admin.register(Song)
class SongCardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'year_of_release',
    )


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
