from django.core.validators import MaxValueValidator
from django.db import models
from datetime import date


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Исполнитель")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Album(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums", verbose_name="Исполнитель")
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска",
                                            validators=[
                                                MaxValueValidator(date.today().year)
                                            ])

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['-year', 'title']


class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    artists = models.ManyToManyField(Artist, related_name='songs', verbose_name='Исполнители')
    albums = models.ManyToManyField(Album, through='AlbumSong', related_name='songs')

    def __str__(self):
        return f"{self.title} by {', '.join(artist.name for artist in self.artists.all())}"

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
        ordering = ['title']


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_number = models.PositiveSmallIntegerField(verbose_name="Порядковый номер в альбоме")

    class Meta:
        unique_together = ('album', 'song_number')
        verbose_name = 'Песня альбома'
        verbose_name_plural = 'Песни альбомов'