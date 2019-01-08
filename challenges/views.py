from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Challenge

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

class ChallengeMainView(ListView):
    model = Challenge
    template_name = 'challenges/challenge_list.html'
    context_object_name = 'challenges'
    ordering = ['-date_created']

class ChallengeDetailView(DetailView):
    model = Challenge

class ChallengeCreateView(CreateView):
    model = Challenge
    fields = ['title', 'description', 'data']

    def form_valid(self, form):
        form.instance.clinician = self.request.user.clinician
        return super().form_valid(form)