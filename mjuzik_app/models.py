from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

GENRE_CHOICES = (
    (-1, 'not defined'),
    (0, 'rock'),
    (1, 'metal'),
    (2, 'pop'),
    (3, 'hip-hop'),
    (4, 'electronic'),
    (5, 'reggae'),
    (6, 'other')
)

STATUS_CHOICES = (
    (1, 'w trakcie pisania'),
    (2, 'czeka na akceptacje'),
    (3, 'opublikowany')
)



class Band(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(default=1, choices=GENRE_CHOICES)




class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    date_started = models.DateField(null=True)
    date_ended = models.DateField(null=True)


class Album(models.Model):
    album_title = models.CharField(max_length=128)
    album_year = models.IntegerField()
    rating = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
