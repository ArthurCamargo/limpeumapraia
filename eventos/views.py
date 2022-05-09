from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Evento

class EventoList(ListView):
    model = Evento
    context_object_name = 'eventos'

class EventoDetail(DetailView):
    model = Evento
    context_object_name = 'evento'
    template_name = 'eventos/evento.html'

class EventoCreate(CreateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('eventos')

class EventoUpdate(UpdateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('eventos')

class EventoDelete(DeleteView):
    model = Evento
    context_object_name = 'evento'
    success_url = reverse_lazy('eventos')