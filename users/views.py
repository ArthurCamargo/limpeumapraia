from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login

from .models import Users


# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='users/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("users:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "users/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "users/register.html",
                  context={"form":form})

def info(request):
    return render(request, 'users/info.html')