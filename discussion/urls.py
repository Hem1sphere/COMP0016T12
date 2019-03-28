from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from .views import(
    DiscussionMainView,
    DiscussionDetailView,
    DiscussionCreateView
    
)
 
urlpatterns = [
    path('', DiscussionMainView.as_view(), name='discussion_main'),
    path('<int:pk>/',DiscussionDetailView.as_view(), name='discussion_detail'),
    path('createDiscussion/', DiscussionCreateView.as_view(), name='discussion_form'),


]
