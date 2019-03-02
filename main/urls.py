from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main, name="main-page"),
    path('tutorial/', views.tutorial, name="tutorial"),
    path('discussion/',include('discussion.urls')),
]