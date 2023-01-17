from django.urls import reverse_lazy
from accounts.forms import CustomUserRegisterForm
from django.views import generic
from django.shortcuts import redirect, render
from .models import CustomUser
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth import views as auth_views

class SignupPageView(generic.CreateView):
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'auth-pages/register.html'

    def form_valid(self, form):
        # Setting is_staff to the users
        form.instance.is_superuser = True
        return super().form_valid(form)