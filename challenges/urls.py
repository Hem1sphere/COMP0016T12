from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
 
urlpatterns = [
    path('', views.ChallengesMainView.as_view(), name='challenges_main'),
    path('detail/', views.ChallengesDetailView.as_view(), name='challenges_detail'),
]