from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # have to set login url in settings

from .models import Movie

class UserLogin(LoginView):
    template_name = "main/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('movies')

class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'

class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'main/movie.html'

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies')

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies')

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')