from django.shortcuts import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


# Create your views here.

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def post(self, request, *args, **kwargs):
        if self.form_class(data=request.POST).is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username,
                                     password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(self.get_success_url())
            else:
                return super(LoginView, self).post(request, *args, **kwargs)
        else:
            return super(LoginView, self).post(request, *args, **kwargs)


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно!'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class LogoutView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LogoutView, self).get_context_data(**kwargs)
        auth.logout(self.request)
        return context




