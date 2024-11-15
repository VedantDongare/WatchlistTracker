from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('create/', views.movie_create, name='movie_create'),
    path('update/<int:movie_id>/', views.movie_update, name='movie_update'),
    path('delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
    path('random/', views.random_movie, name='random_movie'),
]
