from typing import Pattern
from django import urls
from django.urls import path
from django.shortcuts import render, redirect
from home.views import *


#Urls de direccionamiento dentro de la app
urlpatterns = [
    path('', index, name='index'),
    path('proyectos', proyectos, name='proyectos'),
    path('proyecto_detail/<int:pk>', proyecto_detail, name='proyecto_detail'),
    path('contactos/', contactos, name='contactos'),
    path('blog/<int:pk>', blog, name='blog'),
    path('list_blog', list_blog, name='list_blog'),

]
