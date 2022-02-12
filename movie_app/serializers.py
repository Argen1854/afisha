from rest_framework import serializers
from . import models


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = "__all__"


class MovieSerializersList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "id title director".split()


class MovieSerializersDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"