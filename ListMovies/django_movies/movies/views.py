from django.shortcuts import render
from django.views.generic.base import View

from .models import *


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movie_list.html", {"movie_list": movies})






