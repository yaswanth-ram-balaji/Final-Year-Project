from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('upload', views.upload, name='upload'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)