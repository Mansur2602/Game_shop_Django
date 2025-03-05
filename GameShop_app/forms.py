from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Введите действительный email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  



class LoginForm( forms.Form ):
    username = forms.CharField( max_length=100,label="Имя пользователя",widget=forms.TextInput({'placeholder' : 'Имя пользователя'}))
    password = forms.CharField( max_length=100, label='Пароль', widget=forms.PasswordInput({'placeholder' : 'Пароль'}))