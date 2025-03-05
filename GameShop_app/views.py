from django.shortcuts import render, redirect
from .models import Videogame
from django.core.paginator import Paginator, Page
from django.contrib.auth import login,  authenticate, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

def videogame_list(request):
    game_list = Videogame.objects.all()  
    paginator = Paginator(game_list, 6) 
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'GameShop_app/videogame_list.html', {'page': page})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля корректно.')
    else:
        form = RegistrationForm()
    
    return render(request, 'GameShop_app/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home') 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля корректно.')
    else:
        form = LoginForm()

    return render(request, 'GameShop_app/login.html', {'form': form})
