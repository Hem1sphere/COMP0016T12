from django.shortcuts import render
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Solution


def solutions_main(request):
    return render(request, "solutions/solution_submission.html")


class SolutionMainView(ListView):
    model = Solution
    template_name = 'solutions/solution_list.html'
    context_object_name = 'solutions'
    ordering = ['-date_created']

class ChallengeDetailView(DetailView):
    model = Solution

class SolutionCreateView(CreateView):
    model = Solution
    fields = ['developer', 'challenge', 'submission_data']