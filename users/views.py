from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Users

def info(request):
    return render(request, 'users/info.html')