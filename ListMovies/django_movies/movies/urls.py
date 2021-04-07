from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MoviesView.as_view()),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
]


















