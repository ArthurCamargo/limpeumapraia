from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

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


def vote(request, event_id):
    return HttpResponse("You're participating on event %s." % event_id)