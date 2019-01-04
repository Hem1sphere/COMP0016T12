from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
 
urlpatterns = [
    path('', views.solutions_main, name='solutions_main'),
]