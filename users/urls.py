from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.report, name='report'),
    path('index', views.index, name='index'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('loginuser', views.loginUser, name='loginuser'),
    path('logoutuser', views.logoutUser, name='logoutuser'),
]
