from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name='users'
urlpatterns = [
    path('', views.info, name='info'),
    path("register", views.register, name="register"),
    path("login", views.CustomLoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(next_page="eventos:eventos"), name="logout"),
    
]

urlpatterns += staticfiles_urlpatterns()