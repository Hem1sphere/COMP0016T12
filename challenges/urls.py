from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
 
urlpatterns = [
    path('', views.challenges_dev_main, name='challenges_main'),
    path('detail/', views.challenges_dev_detail, name='challenges_detail'),
]