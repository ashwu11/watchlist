from django.urls import path
from .views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDelete, UserLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLogin.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('', MovieList.as_view(), name = 'movies'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name = 'movie'), 
    path('create/', MovieCreate.as_view(), name = 'create'),
    path('edit/<int:pk>/', MovieUpdate.as_view(), name = 'edit'),
    path('delete/<int:pk>/', MovieDelete.as_view(), name = 'delete'),
]