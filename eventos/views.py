from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Evento

class EventoList(ListView):
    model = Evento
    context_object_name = 'eventos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['eventos'] = context['eventos'].filter(
                name__startswith=search_input)
        
        context['search_input'] = search_input

        return context

class HomeView(ListView):
    model = Evento
    template_name='eventos/home.html'
    context_object_name = 'eventos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['eventos'] = context['eventos'].order_by('event_date')  
        context['eventos'] = context['eventos'][0:4]

        return context

class EventoDetail(DetailView):
    model = Evento
    context_object_name = 'evento'
    template_name = 'eventos/evento.html'


class EventoUserList(LoginRequiredMixin, ListView):
    model = Evento
    context_object_name = 'eventos'
    template_name = 'eventos/evento_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = context['eventos'].filter(creator=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['eventos'] = context['eventos'].filter(
                name__startswith=search_input)
        
        context['search_input'] = search_input

        return context

class EventoCreate(LoginRequiredMixin, CreateView):
    model = Evento
    fields = ['name', 'event_date', 'descr_text', 'city_text',
              'location_map', 'type_event', 'banner']
    success_url = reverse_lazy('eventos:evento-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(EventoCreate, self).form_valid(form)

class EventoUpdate(LoginRequiredMixin, UpdateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('eventos:evento-list')

class EventoDelete(LoginRequiredMixin, DeleteView):
    model = Evento
    context_object_name = 'evento'
    success_url = reverse_lazy('eventos:evento-list')