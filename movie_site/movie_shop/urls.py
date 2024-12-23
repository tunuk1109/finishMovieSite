from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'rating', RatingViewSet, basename='rating_list'),
router.register(r'favorite', FavoriteViewSet, basename='favorite_list'),
router.register(r'history', HistoryViewSet, basename='history_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('users/', ProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', ProfileDetailAPIView.as_view(), name='user_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('directors/', DirectorListAPIView.as_view(), name='director_list'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actors/', ActorListAPIView.as_view(), name='actor_list'),
    path('actors/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('genres/', GenreListAPIView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]