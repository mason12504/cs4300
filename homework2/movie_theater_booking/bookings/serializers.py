# part of rest framework 

from rest_framework import serializers
from bookings.models import Movie # Other things too but just fo now


class MovieSerializer(serializers.Serializer):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    release_date = models.DateTimeField("date published")
    duration = models.IntegerField(default=0)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance