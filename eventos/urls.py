from django.urls import path

from .views import EventoList, EventoCreate, EventoDetail
from .views import  EventoUpdate, EventoDelete, EventoUserList
from .views import HomeView

app_name ='eventos'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('evento-list', EventoList.as_view(), name='evento-list'),
    path('evento/<int:pk>/', EventoDetail.as_view(), name='evento'),
    path('evento-user', EventoUserList.as_view(), name='evento-user'),
    path('evento-create/', EventoCreate.as_view(), name = 'evento-create'),
    path('evento-update/<int:pk>/', EventoUpdate.as_view(), name='evento-update'),   
    path('evento-delete/<int:pk>/', EventoDelete.as_view(), name='evento-delete'),   
]