from django.shortcuts import render

# Create your views here.
from .models import Challenge
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class ChallengesMainView(ListView):
    model = Challenge
    template_name = 'challenges/challenges_developers_main.html'

class ChallengesDetailView(DetailView):
    model = Challenge