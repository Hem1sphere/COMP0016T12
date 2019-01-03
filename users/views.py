from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect
from .models import User
from .forms import DeveloperRegisterForm
from .forms import ClinicianRegisterForm


# Create your views here.
class RegisterView(TemplateView):
    template_name = "users/register.html"


class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegisterForm
    template_name = 'users/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'developer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


class ClinicianRegisterView(CreateView):
    model = User
    form_class = ClinicianRegisterForm
    template_name = 'users/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'clinician'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')
