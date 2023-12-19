from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm


# Create your views here.
class Login(LoginView):
    template_name = 'users_app/login.html'
    next_page = 'question'


class Logout(LogoutView):
    next_page = 'login'


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'users_app/profile.html'


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'users_app/signup.html', context={'form': form})
