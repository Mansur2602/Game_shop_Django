from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название жанра')

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название компаний разработчиков')

    def __str__(self):
        return self.name

class Videogame(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название игры')
    description = models.CharField(max_length=500, verbose_name='Описание игры')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата выхода')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр игры')
    image = models.ImageField(upload_to='games/', verbose_name='Изображение')
    developers = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True, verbose_name='Разработчики')

    def __str__(self):
        return self.title
