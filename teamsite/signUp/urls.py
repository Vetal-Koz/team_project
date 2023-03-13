from django.urls import path, include
from . import views
#from .forms import UserLoginForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.signup, name='signUp'),
    #path('login/', LoginView.as_view(template_name="login1.html", authentication_form=UserLoginForm), name='login')
    path('logins/', views.login, name='login'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]