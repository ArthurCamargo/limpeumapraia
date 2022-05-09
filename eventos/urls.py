from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import EventoList, EventoCreate, EventoDetail 

app_name= 'eventos'
urlpatterns = [
    path('', EventoList.as_view(), name='eventos'),
    path('evento/<int:pk>/', EventoDetail.as_view(), name='evento'),
    path('evento-create', EventoCreate.as_view(), name='evento-create'),
] 

urlpatterns += staticfiles_urlpatterns()