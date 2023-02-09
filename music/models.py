from datetime import date
from django.db import models


class Performer(models.Model):
    title = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.title


class Album(models.Model):
    performer = models.ForeignKey(
        'Performer',
        related_name='albums',
        on_delete=models.CASCADE
    )
    year_of_release = models.DateField(default=date.today)
    songs = models.ManyToManyField(
        'Song',
        related_name='songs'
    )

    def __str__(self):
        return f'{self.year_of_release}'


class Song(models.Model):
    title = models.CharField('Song', max_length=50)

    def __str__(self):
        return self.title
