from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from blog.views import (mostrar_inicio, procesar_formulario_autor, procesar_formulario_articulo, buscar_autor, AutorList, PaginasList, AutorDetalle, PaginaDetalle, AutorCreacion, PaginaCreacion, AutorUpdateView, PaginaUpdateView, AutorDelete, PaginaDelete,  MyLogin, MyLogout, register, editar_perfil, agregar_avatar, about_me)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('inicio/', mostrar_inicio, name="home"),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("buscar-autor/", buscar_autor, name="buscar_autor"),
    path("autor/list", AutorList.as_view(), name="AutorList"),
    path("paginas/list", PaginasList.as_view(), name="PaginasList"),
    path("r'(?P<pk>\d+)^$'", AutorDetalle.as_view(), name="AutorDetail"),
    path("detalle/<pk>", PaginaDetalle.as_view(), name="PaginaDetail"),
    path("autor-nuevo/", AutorCreacion.as_view(), name="AutorNew"),
    path("pagina-nuevo/", PaginaCreacion.as_view(), name="PaginaNew"),
    path(r'^editar/(?P<pk>\d+)$', AutorUpdateView.as_view(), name="AutorUpdate"),
    path("editar/<pk>", PaginaUpdateView.as_view(), name="PaginaUpdate"),
    path("borrar/<pk>", PaginaDelete.as_view(), name="PaginaDelete"),
    path(r'^borrar/(?P<pk>\d+)$', AutorDelete.as_view(), name="AutorDelete"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    path("profile/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    path("", mostrar_inicio),
    path("about/", about_me , name="About"),
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)