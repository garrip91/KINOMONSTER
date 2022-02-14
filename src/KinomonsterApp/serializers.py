from rest_framework import serializers
from .models import Film, FilmComments



class FilmListSerializer(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = Film
        fields = ('title', 'logo', 'youtube_trailer_url', 'year', 'rating', 'producer', 'description')
        
        
class FilmCommentsCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""
    
    class Meta:
        model = FilmComments
        fields = '__all__'