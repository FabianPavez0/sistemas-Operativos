from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.crear_socio),
    path('<str:dni>/', views.modificar_contraseña),
    path('', views.obtener_todos_socios),
]
