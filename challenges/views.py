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

def challenge(request):
    context = {
        'challenges': Challenge.objects.all()
    }
    return render(request, 'challenges/challenge_list.html', context)

class ChallengesMainView(ListView):
    model = Challenge
    template_name = 'challenges/challenge_list.html'
    context_object_name = 'challenges'

class ChallengesDetailView(DetailView):
    model = Challenge
