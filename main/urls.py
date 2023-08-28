from django.urls import path
from .views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDelete

urlpatterns = [
    path('', MovieList.as_view(), name = 'movies'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name = 'movie'), 
    path('create/', MovieCreate.as_view(), name = 'create'),
    path('edit/<int:pk>/', MovieUpdate.as_view(), name = 'edit'),
    path('delete/<int:pk>/', MovieDelete.as_view(), name = 'delete'),
]