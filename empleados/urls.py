from django.urls import path
from . import views

urlpatterns = [
    # Cambiamos la URL de empleados a la raíz para acceder directamente
    path('', views.lista_empleados, name='lista_empleados'),
]