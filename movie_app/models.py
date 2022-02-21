from enum import _auto_null
from random import choices
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.directors.all().count()

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description =  models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='directors')

    def __str__(self):
        return self.title

    @property
    def reviews_count(self):
        review = Review.objects.filter(movie = self)
        return [{'id': i.id, 'text': i.text, 'stars': i.stars} for i in review]

    @property
    def rating_count(self):
        p = 0
        for i in self.reviews_move.all():
            p += int(i.stars)
        return p/self.reviews_move.all().count()


class Review(models.Model):
    STAR = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews_move')
    stars = models.CharField(max_length=100, choices=STAR, null=True)

    def __str__(self):
        return self.movie.title