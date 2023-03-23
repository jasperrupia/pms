from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='signin'),
    path('logout', views.user_logout),
    path('recover', views.recover),
    path('register', views.register, name='register'),
    path('registerUser', views.registerUser),
]
