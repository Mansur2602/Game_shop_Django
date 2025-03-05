from django.contrib import admin
from .models import Genre, Videogame, Developer

admin.site.register([Genre, Videogame, Developer])
