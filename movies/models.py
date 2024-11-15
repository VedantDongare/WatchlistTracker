from django.db import models

# Create your models here.

# movies/models.py

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=50, blank=True)
    rating = models.IntegerField(default=0)  # Rating out of 10
    watched = models.BooleanField(default=False)  # Watched toggle
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
