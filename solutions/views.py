from django.shortcuts import render
# Create your views here.
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Solution


def solution(request):
    context = {
        'solutions': Solution.objects.all()
    }
    return render(request, 'solutions/solution_list.html', context)


class SolutionMainView(ListView):
    model = Solution
    template_name = 'solutions/solution_list.html'
    context_object_name = 'solutions'
    ordering = ['-date_created']

class SolutionDetailView(DetailView):
    model = Solution

class SolutionCreateView(CreateView):
    model = Solution
    fields = ['title', 'description', 'challenge', 'solution_data']

    def form_valid(self, form):
        form.instance.developer = self.request.user.developer
        form.save()
        return super(SolutionCreateView, self).form_valid(form)


class SolutionUpdateView(UserPassesTestMixin, UpdateView):
    model = Solution
    fields = ['title', 'description', 'solution_data']

    def form_valid(self, form):
        form.instance.developer = self.request.user.developer
        return super(SolutionUpdateView, self).form_valid(form)

    def test_func(self):
        solution = self.get_object()
        if self.request.user.developer == solution.developer:
            return True
        return False


class SolutionDeleteView(UserPassesTestMixin, DeleteView):
    model = Solution
    success_url = '/'

    def test_func(self):
        solution = self.get_object()
        if self.request.user.developer == solution.developer:
            return True
        return False