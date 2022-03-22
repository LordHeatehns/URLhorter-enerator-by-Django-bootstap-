from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import home_view ,redirect_url_view


urlpatterns = [
    path('',home_view,name="home"),
    path('<str:shorter_part>/',redirect_url_view , name ='shorter')
]
