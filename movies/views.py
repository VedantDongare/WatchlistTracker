from django.shortcuts import render

# Create your views here.

# movies/views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Movie
from django.http import HttpResponse

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        rating = request.POST.get('rating')
        watched = request.POST.get('watched') == 'on'
        movie = Movie.objects.create(title=title, description=description, genre=genre, rating=rating, watched=watched)
        return redirect('movie_list')
    return render(request, 'movies/movie_form.html')

def movie_update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.description = request.POST.get('description')
        movie.genre = request.POST.get('genre')
        movie.rating = request.POST.get('rating')
        movie.watched = request.POST.get('watched') == 'on'
        movie.save()
        return redirect('movie_list')
    return render(request, 'movies/movie_form.html', {'movie': movie})

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movie_list')

# Random movie pick feature
import random

def random_movie(request):
    # Fetch all movies
    all_movies = Movie.objects.all()

    # If there are movies, select a random one
    if all_movies:
        movie = random.choice(all_movies)  # Randomly selects a movie from the queryset
    else:
        movie = None  # No movies in the database

    return render(request, 'movies/random_movie.html', {'movie': movie})