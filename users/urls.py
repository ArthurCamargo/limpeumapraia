from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, RegisterPage

app_name='users'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='eventos:eventos'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]
urlpatterns += staticfiles_urlpatterns()