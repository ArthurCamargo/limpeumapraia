from django import forms
from location_field.forms.plain import PlainLocationField
from eventos.models import Evento

class EventoForm(forms.Form):
    # declare the fields you will show

    name = forms.CharField(max_length=255, label="Nome:")
    event_date = forms.DateTimeField(widget=forms.DateTimeInput(), label="Data")
    descr_text = forms.CharField(widget=forms.Textarea(),label="Descrição")
    location_map = PlainLocationField()
    type_event = forms.CharField(max_length=40)

    # this sets the order of the fields
    class Meta:
        model = Evento
        fields = ("name", "event_date", "descr_text", "city_text", "location_map", "type_event")