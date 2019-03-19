from django.urls import path
from .views import (
    TutorialCreateView,
    TutorialMainView
)

urlpatterns = [
    path('', TutorialMainView.as_view(), name='tutorial_main'),
    path('create/', TutorialCreateView.as_view(), name='tutorial_create')
]