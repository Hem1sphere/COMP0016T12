from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Tutorial
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
class TutorialMainView(ListView):
    model = Tutorial
    template_name = 'tutorial/tutorial_list.html'
    context_object_name = 'tutorial'
    ordering = ['-date_created']


class TutorialCreateView(SuccessMessageMixin, CreateView):
    model = Tutorial
    fields = ['title',  'prerequisites', 'description', 'data']
    success_message = "The tutorial has been successfully created."

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        return super(TutorialCreateView, self).form_valid(form)

