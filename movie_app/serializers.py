from rest_framework import serializers
from . import models


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = "id name movies_count".split()


class MovieSerializersList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "id title description duration director".split()

class MoviesSerializersList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = 'id title description duration director reviews_count rating_count'.split()

class MovieSerializersDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"