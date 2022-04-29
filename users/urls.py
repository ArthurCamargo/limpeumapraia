from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.info, name='info'),
]

urlpatterns += staticfiles_urlpatterns()