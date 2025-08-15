from django.contrib import admin
from .models import Artist, Album, Song, AlbumSong


admin.site.site_header = 'Музыкальный каталог'


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    ordering = ['name']
    search_fields = ['name__istartswith']
    fields = ['name']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist', 'title', 'year']
    list_display_links = ['title']
    ordering = ['year', 'title']
    search_fields = ['title__istartswith', 'artist__name__istartswith']
    fields = ['title', 'artist', 'year']


class AlbumSongInline(admin.TabularInline):
    model = AlbumSong
    fields = ['album', 'song_number']
    extra = 1


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_artists', 'display_albums']
    list_display_links = ['title']
    ordering = ['artists', 'title']
    search_fields = ['title__istartswith', 'artists__name__istartswith', 'albums__title__istartswith']
    fields = ['title', 'artists']
    inlines = [AlbumSongInline]

    @admin.display(description='Исполнители')
    def display_artists(self, obj):
        return ', '.join([artist.name for artist in obj.artists.all()])

    @admin.display(description='Альбомы')
    def display_albums(self, obj):
        return ', '.join([album.title for album in obj.albums.all()])