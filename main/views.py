from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Movie

class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'

class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'main/movie.html'

class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies') # redirects backs to this page 