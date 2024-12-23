from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class CountryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class RatingSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%Y-%m-%d %H:%M'))
    user = ProfileSimpleSerializers()

    class Meta:
        model = Rating
        fields = ['id', 'user', 'stars', 'parent', 'text', 'created_date']


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class MovieListSerializers(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    genre = GenreListSerializers(many=True)
    country = CountryListSerializers(many=True)


    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image',  'year', 'genre', 'country', 'status']


class MovieDetailSerializers(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    director = DirectorListSerializers(many=True)
    actor = ActorListSerializers(many=True)
    genre = GenreListSerializers(many=True)
    country = CountryListSerializers(many=True)
    movie_languages = MovieLanguagesSerializers(many=True, read_only=True)
    movie_moments = MomentsSerializers(many=True, read_only=True)
    ratings = RatingSerializers(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image', 'year', 'director', 'actor',
                  'genre', 'country', 'types', 'movie_time', 'description', 'movie_trailer',
                  'status', 'movie_languages', 'movie_moments', 'ratings', 'get_avg_rating']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

class CountryDetailSerializers(serializers.ModelSerializer):
    movies = MovieListSerializers(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'movies']


class DirectorDetailSerializers(serializers.ModelSerializer):
    directors = MovieListSerializers(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['director_name', 'directors']


class ActorDetailSerializers(serializers.ModelSerializer):
    actors = MovieListSerializers(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['actor_name', 'actors']


class GenreDetailSerializers(serializers.ModelSerializer):
    genres = MovieListSerializers(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name', 'genres']


class HistorySerializers(serializers.ModelSerializer):
    user = ProfileSimpleSerializers()
    movie = MovieListSerializers()
    viewed_at = serializers.DateTimeField(format('%Y-%m-%d %H:%M'))

    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']




































