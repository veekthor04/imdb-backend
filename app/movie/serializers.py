from rest_framework import serializers

from core.models import Movie, UserMovieBookmark


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(max_value=10, min_value=0)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'rating']

    def create(self, validated_data):
        return super().create(validated_data)


class UserMovieBookmarkSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    
    class Meta:
        model = UserMovieBookmark
        fields = ['movies']
        
