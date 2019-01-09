from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from .views import(
    ChallengeDetailView,
    ChallengeMainView,
    ChallengeCreateView,
    ChallengeUpdateView,
    ChallengeDeleteView
)
 
urlpatterns = [
    path('', ChallengeMainView.as_view(), name='challenges_main'),
    path('<int:pk>/', ChallengeDetailView.as_view(), name='challenges_detail'),
    path('create/', ChallengeCreateView.as_view(), name = 'challenges_create'),
    path('<int:pk>/update', ChallengeUpdateView.as_view(), name = 'challenges_update'),
    path('<int:pk>/delete', ChallengeDeleteView.as_view(), name = 'challenges_delete')
]