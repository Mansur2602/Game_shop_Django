from django.shortcuts import render, redirect
from .models import Videogame, Cart, CartItem, Videogame, Purchase, PurchaseSerializer
from django.core.paginator import Paginator, Page
from django.contrib.auth import login,  authenticate, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


def videogame_list(request):
    query = request.GET.get('search', '')  
    game_list = Videogame.objects.all() 

    if query:  #Функционал поиска
        game_list = game_list.filter(title__icontains=query)

    paginator = Paginator(game_list, 6)  
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    no_results = not game_list.exists() 
    
    return render(request, 'GameShop_app/videogame_list.html', {'page': page, 'query': query, 'no_results': no_results  })



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('videogame_list')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля корректно.')
    else:
        form = RegistrationForm()
    
    return render(request, 'GameShop_app/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('videogame_list') 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('videogame_list') 
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля корректно.')
    else:
        form = LoginForm()

    return render(request, 'GameShop_app/login.html', {'form': form})





@login_required
def add_to_cart(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        game = Videogame.objects.get(id=game_id)

        cart, created = Cart.objects.get_or_create(user=request.user, active=True)

    
        cart_item = CartItem.objects.filter(cart=cart, game=game).first()

        if not cart_item:
            cart_item = CartItem(cart=cart, game=game, quantity=1)
            cart_item.save()
        else:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('videogame_list')   


@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first()  
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_sum = sum(item.game.price * item.quantity for item in cart_items)

    if request.method == "POST":
        print("wwwqwew")

        qweqw = 123123
        if qweqw != None:
            print("wwww")
            items = CartItem.objects.filter(cart=cart).all()
            for item in items:
                Purchase.objects.create(user=request.user, game = item.game)
                print(item.game.title)
                item.delete()
                

    return render(request, 'GameShop_app/cart.html', {
        'cart_items': cart_items,
        'total_sum': total_sum
    })


@login_required
def remove_from_cart(request, item_id): 
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.delete()
        messages.success(request, "Товар удален из корзины!")
    except CartItem.DoesNotExist:
        messages.error(request, "Товар не найден в вашей корзине или уже был удален.")
    
    return redirect('cart_view')


class PurchaseListView(APIView):
    def get(self, request):
        purchases = Purchase.objects.filter(user = request.user) 
        serializer = PurchaseSerializer(purchases, many=True) 
        return JsonResponse(serializer.data, safe=False)