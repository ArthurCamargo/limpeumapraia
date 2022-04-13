from django.urls import path

from . import views

app_name= 'eventos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    path('<int:event_id>/participate/', views.participate, name='participate'),
]