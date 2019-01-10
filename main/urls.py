from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main-page"),
    path('tutorial/', views.tutorial, name="tutorial")
]