from django.urls import path

from .views import EventoList, EventoCreate, EventoDetail, EventoUpdate, EventoDelete 

urlpatterns = [
    path('', EventoList.as_view(), name='eventos'),
    path('evento/<int:pk>/', EventoDetail.as_view(), name='evento'),
    path('evento-create/', EventoCreate.as_view(), name = 'evento-create'),
    path('evento-update/<int:pk>/', EventoUpdate.as_view(), name='evento-update'),   
    path('evento-delete/<int:pk>/', EventoDelete.as_view(), name='evento-delete'),   

]