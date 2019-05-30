from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
]