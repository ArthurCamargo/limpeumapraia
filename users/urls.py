from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.info, name='info'),
    path("register", views.register, name="register"),
    path("home", views.homepage, name="homepage"),
    
]

urlpatterns += staticfiles_urlpatterns()