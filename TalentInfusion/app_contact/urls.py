from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('contact', views.contact, name="contact page"),
    path('about', views.about, name="about page"),
]