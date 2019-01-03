from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect
from .models import User
from .forms import DeveloperRegisterForm
from .forms import ClinicianRegisterForm

# from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import developer_required


@login_required
@developer_required
def testrestricted(request):
    return HttpResponse('<h1>test restricted views for developer</h1>')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


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
