from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Evento(models.Model):
    TYPE_CHOICES = ( 
        ("C", "Competicao"),
        ("W", "Workshop"),
        ("P", "Palestra"),
        ("T", "Tradicional"),
    )

    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    event_date = models.DateTimeField('event date')
    descr_text = models.CharField('description', max_length=5000)
    city_text = models.CharField(max_length=255)
    location_map = PlainLocationField(based_fields=['city'], zoom=7)
    type_event = models.CharField(max_length=40, choices=TYPE_CHOICES)
    part_number = models.IntegerField(default=0)
    banner = models.ImageField(upload_to='banners')

    def __str__(self):
        return self.name
