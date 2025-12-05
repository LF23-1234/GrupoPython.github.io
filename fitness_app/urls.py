from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entrenadores/', views.entrenadores, name='entrenadores'),
    path('articulos/', views.articulos, name='articulos'),
    path('contactos/', views.contactos, name='contactos'),
    path('habitos-progreso/', views.habitos_progreso, name='habitos_progreso'),

    # LOGIN
    path('login/', views.custom_login, name='login'),
    path('login.html', views.custom_login),

    # REGISTER
    path('register/', views.register, name='register'),
    path('register.html', views.register),

    # PROFILE
    path('profile/', views.profile, name='profile'),

    # LOGOUT (CORRECCIÓN)
    path('logout/', views.custom_logout, name='logout'),
]
