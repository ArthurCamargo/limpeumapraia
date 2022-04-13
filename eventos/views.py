from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Evento

def index(request):
    latest_events_list = Evento.objects.order_by('-pub_date')[:5]
    context = {
        'latest_events_list': latest_events_list,
    }
    return render(request, 'eventos/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Evento, pk=event_id)
    return render(request, 'eventos/detail.html', {'event' : event})


def participate(request, event_id):
    event = get_object_or_404(Evento, pk=event_id)
    event.part_number += 1
    event.save()


    return HttpResponseRedirect(reverse('eventos:detail', args=(event.id,)))