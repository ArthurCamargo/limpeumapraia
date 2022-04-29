from django.db import models
from django.contrib.auth.models import User
import eventos.models

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='avatars')
    eventos = models.ForeignKey(eventos.models.Evento, on_delete=models.CASCADE)
