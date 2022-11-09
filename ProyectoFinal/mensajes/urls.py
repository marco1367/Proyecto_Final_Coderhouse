from django.urls import path
from mensajes.views import inicioMensajeria

urlpatterns = [
    path('', inicioMensajeria, name="InicioMensajeria"),
]


