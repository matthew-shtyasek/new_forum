from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

app_name = 'custom_auth'

urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='auth/sign-in.html'), name='sign-in'),
    path('sign-up/', CreateView.as_view(template_name='auth/sign-up.html',
                                        success_url=reverse_lazy('auth:sign-in'),
                                        form_class=UserCreationForm,
                                        model=User), name='sign-up')
]
