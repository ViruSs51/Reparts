from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_redirect, name='authentication'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]
