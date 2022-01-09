from typing import Pattern
from django import urls
from django.urls import path
from django.shortcuts import render, redirect
from home.views import *


#Urls de direccionamiento dentro de la app
urlpatterns = [
    path('', index, name='index'),

]
