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
from django import forms
from .models import Solution
from .models import Challenge
from challenges.templatetags import template_methods
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import sys
from nbconvert import HTMLExporter
import nbformat


def solution(request):
    context = {
        'solutions': Solution.objects.all()
    }
    return render(request, 'solutions/solution_list.html', context)


def notebookconverthtml(nbfile, htmlfile):
    html_exporter = HTMLExporter()
    nb = nbformat.reads(open(nbfile, 'r').read(), as_version=4)
    (body, resources) = html_exporter.from_notebook_node(nb)
    htmlfile = nbfile.replace(".ipynb", ".html")
    html_file_writer = open(htmlfile, 'w')
    html_file_writer.write(body)
    html_file_writer.close()


class SolutionMainView(ListView):
    model = Solution
    template_name = 'solutions/solution_list.html'
    context_object_name = 'solutions'
    ordering = ['-date_created']


class SolutionDetailView(DetailView):
    model = Solution


class SolutionForm(forms.ModelForm):
    class Meta:
        model=Solution
        fields=['title', 'description', 'challenge', 'solution_data']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        challengepk = kwargs.pop('challengepk', None)
        super(SolutionForm, self).__init__(*args, **kwargs)
        self.fields['challenge'].queryset = user.developer.challenge_set.all()
        if challengepk != 0:
            print("PK is " + challengepk + ", and this line should not be executed/printed")
            self.fields['challenge'].initial = Challenge.objects.get(pk=challengepk)

class SolutionEvaluationForm(forms.ModelForm):
    class Meta:
        model=Solution
        fields=['title', 'description', 'challenge', 'solution_data', 'accuracy']

    def __init__(self, *args, **kwargs):
        super(SolutionEvaluationForm, self).__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['description'].disabled = True
        self.fields['challenge'].disabled = True
        self.fields['solution_data'].disabled = True


class SolutionCreateView(SuccessMessageMixin, CreateView):
    template_name = 'solutions/solution_form.html'
    form_class = SolutionForm
    success_message = "The solution has been successfully created."

    def get_form_kwargs(self):
        kwargs = super(SolutionCreateView, self).get_form_kwargs()
        kwargs ['user'] = self.request.user
        kwargs ['challengepk'] = self.kwargs['challengepk']
        return kwargs

    def form_valid(self, form):
        form.instance.developer = self.request.user.developer
        notebookconverthtml(form.instance.solution_notebook_htmlver, form.instance.solution_notebook_htmlver)
        return super(SolutionCreateView, self).form_valid(form)


class SolutionUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Solution
    fields = ['title', 'description', 'solution_data']
    success_message = "The solution has been successfully updated."

    def form_valid(self, form):
        form.instance.developer = self.request.user.developer
        return super(SolutionUpdateView, self).form_valid(form)

    def test_func(self):
        solution = self.get_object()
        if self.request.user.developer == solution.developer:
            return True
        return False


class SolutionEvaluateView(UserPassesTestMixin, UpdateView):
    model = Solution
    template_name_suffix = "_evaluate_form"
    form_class = SolutionEvaluationForm

    def test_func(self):
        solution = self.get_object()
        if self.request.user.clinician == solution.challenge.clinician:
            return True
        return False


class SolutionDeleteView(UserPassesTestMixin, DeleteView):
    model = Solution
    success_url = '/'
    success_message = 'The solution has been successfully deleted.'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SolutionDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        solution = self.get_object()
        if self.request.user.developer == solution.developer:
            return True
        return False