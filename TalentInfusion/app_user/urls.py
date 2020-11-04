from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('reg',views.reg, name='register user'),
    path('signin', views.signin, name='signin user'),
]
