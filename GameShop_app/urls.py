from django.urls import path
from .views import videogame_list, register, logout_view, login_view
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('', videogame_list, name='home'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login', login_view, name='login')
    
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)