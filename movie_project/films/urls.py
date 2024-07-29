from django.urls import path
from . import views


urlpatterns = [
    path('films/', views.films_list, name='film_list'),
]