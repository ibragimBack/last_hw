from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from . import forms


class RegisterView(CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'register_and_authorization/register.html'
    success_url = '/'


class AuthorizationView(LoginView):
    form_class = AuthenticationForm
    template_name = 'register_and_authorization/login.html'

    def get_success_url(self):
        return reverse('person:book_list')


class OutLogoutView(LogoutView):
    next_page = reverse_lazy('person:login')
