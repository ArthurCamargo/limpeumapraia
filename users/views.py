from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic.edit import FormView
from django.contrib.auth import login

from .forms import RegisterForm

from django.urls import reverse_lazy

from .models import NewUser


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('eventos:eventos')


class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('eventos:eventos')

    def form_valid(self , form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('eventos:eventos')
        return super(RegisterPage, self).get(*args, **kwargs)
