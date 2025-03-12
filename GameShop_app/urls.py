from django.urls import path
from .views import videogame_list, register, logout_view, login_view, add_to_cart, cart_view, remove_from_cart, PurchaseListView
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('', videogame_list, name='videogame_list'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('cart/', cart_view, name='cart_view' ),
    path('add_to_cart/',add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/',remove_from_cart, name='remove_from_cart'),
    path('api_purchases/', PurchaseListView.as_view(), name='api_purchases')
    
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)