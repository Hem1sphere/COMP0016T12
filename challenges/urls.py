from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from .views import (
    ChallengeMainView,
    ChallengeCreateView,
    ChallengeUpdateView,
    ChallengeDeleteView,
    ChallengeOverviewView,
    ChallengeDataView,
    ChallengeDiscussionView,
    ChallengeLeaderboardView,
    ChallengeRulesView,
    ChallengeSolutionsView
)

urlpatterns = [
    path('', ChallengeMainView.as_view(), name='challenges_main'),
    path('<int:pk>/', ChallengeOverviewView.as_view(), name='challenges_detail'),
    path('create/', ChallengeCreateView.as_view(), name='challenges_create'),
    path('<challengeid>/participate', views.participateInChallenge, name='participate'),
    path('<challengeid>/leavechallenge', views.leaveChallenge, name='leave'),
    path('<int:pk>/update', ChallengeUpdateView.as_view(), name='challenges_update'),
    path('<int:pk>/delete', ChallengeDeleteView.as_view(), name='challenges_delete'),
    path('<int:pk>/overview', ChallengeOverviewView.as_view(), name='challenges_overview'),
    path('<int:pk>/data', ChallengeDataView.as_view(), name='challenges_data'),
    path('<int:pk>/solutions', ChallengeSolutionsView.as_view(), name='challenges_solutions'),
    path('<int:pk>/discussion', ChallengeDiscussionView.as_view(), name='challenges_discussion'),
    path('<int:pk>/leaderboard', ChallengeLeaderboardView.as_view(), name='challenges_leaderboard'),
    path('<int:pk>/rules', ChallengeRulesView.as_view(), name='challenges_rules')

]
