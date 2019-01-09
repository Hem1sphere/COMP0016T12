from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from .views import (
    SolutionCreateView,
    SolutionDetailView,
    SolutionDeleteView,
    SolutionMainView,
    SolutionUpdateView
)
 
urlpatterns = [
    path('', SolutionMainView.as_view(), name='solutions_main'),
    path('<int:pk>/', SolutionDetailView.as_view(), name='solutions_detail'),
    path('create/', SolutionCreateView.as_view(), name = 'solutions_create'),
    path('<int:pk>/update', SolutionUpdateView.as_view(), name = 'solutions_update'),
    path('<int:pk>/delete', SolutionDeleteView.as_view(), name = 'solutions_delete')
]