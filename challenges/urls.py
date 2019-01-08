from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from .views import(
    ChallengesDetailView,
    ChallengesMainView
)
 
urlpatterns = [
    path('', ChallengesMainView.as_view(), name='challenges_main'),
    path('<int:pk>', ChallengesDetailView.as_view(), name='challenges_detail'),
]