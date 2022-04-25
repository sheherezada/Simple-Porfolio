from django.views import generic as views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.urls import reverse_lazy

from PROJECT.accounts.forms import CreateProfileForm
from PROJECT.common.view_mixin import RedirectToDashboard


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('show index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super.get_success_url()


def logout(request):
    auth_logout(request)
    return render(request, "index.html")
