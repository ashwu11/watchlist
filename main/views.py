from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # have to set login url in settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Movie

class UserLogin(LoginView):
    template_name = "main/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('movies')

class UserRegistration(FormView):
    template_name = "main/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('movies')

    # automatically login the created user 
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegistration, self).form_valid(form)
    
    # block registration page if user is logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('movies')
        return super(UserRegistration, self).get(*args, **kwargs)

class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = context['movies'].filter(user = self.request.user)
        context['count'] = context['movies'].filter(status = False).count()

        search_input = self.request.GET.get('search-text') or ''
        if search_input:
            context['movies'] = context['movies'].filter(title__icontains = search_input) # or title__startswith

        context['search_input'] = search_input

        return context

class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'main/movie.html'

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'type', 'description', 'status']
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self.form_valid)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['title', 'type', 'description', 'status', 'rating']
    success_url = reverse_lazy('movies')

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')