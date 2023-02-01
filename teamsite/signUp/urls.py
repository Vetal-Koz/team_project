from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signUp'),
    path('logIn', views.login, name='about')
]