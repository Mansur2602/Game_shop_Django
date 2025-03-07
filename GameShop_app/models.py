from django.db import models
from django.contrib.auth.models import User

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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания корзины')
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"Корзина пользователя {self.user.username} ({self.created_at})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, verbose_name='Корзина')
    game = models.ForeignKey(Videogame, on_delete=models.CASCADE, verbose_name='Игра')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    
    def __str__(self):
        return f"{self.game.title} x{self.quantity} в корзине {self.cart.user.username}"

    def get_total_price(self):
        return self.game.price * self.quantity
