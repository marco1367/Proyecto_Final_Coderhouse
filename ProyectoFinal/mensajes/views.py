from django.shortcuts import render

# Create your views here.
def inicioMensajeria(request):
    return render(request, "mensajes/inicio.html")