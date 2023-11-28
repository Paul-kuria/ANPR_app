from django.contrib import admin
from django.urls import path 
from . import views 
urlpatterns = [
    path("", views.home, name="home"),
    path("residents/", views.residents, name="residents"),
    path("activity/", views.activity, name="activity"),
]
