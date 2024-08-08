from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.CharField(max_length=100, blank=True)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
