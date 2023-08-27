from django.urls import path
from .views import MovieList, MovieDetail, MovieCreate

urlpatterns = [
    path('', MovieList.as_view(), name = 'movies'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name = 'movie'), 
    path('create/', MovieCreate.as_view(), name = 'create'),
]