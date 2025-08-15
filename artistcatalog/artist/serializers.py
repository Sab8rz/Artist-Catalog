from django.db.models.fields.related import RelatedField
from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class SongSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    albums = serializers.StringRelatedField(many=True, source='albums.all')

    class Meta:
        model = Song
        fields = ['id', 'title', 'artists', 'albums']


class AlbumSongSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField()
    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all())

    class Meta:
        model = AlbumSong
        fields = ['song', 'song_id','song_number']


class AlbumSerializer(serializers.ModelSerializer):
    songs = AlbumSongSerializer(many=True, source='albumsong_set')

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'year', 'songs']