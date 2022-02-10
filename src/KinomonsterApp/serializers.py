from rest_framework import serializers
from .models import Film



class FilmListSerializer(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = Film
        fields = ('title', 'logo', 'youtube_trailer_url', 'year', 'rating', 'producer', 'description')