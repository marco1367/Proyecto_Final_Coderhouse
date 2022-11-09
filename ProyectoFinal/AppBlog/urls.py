from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    ##Usuario
    path('login', Login.as_view(), name="Login"),
    path('logout', Logout.as_view(), name="LogOut"),
    path("profile", editar_perfil, name="EditarPerfil"),
    path("register", register, name="Register"),
    path("agregar-avatar", agregar_avatar, name="AgregarAvatar"),
    ##Autor
    path("autor-nuevo", AutorCreacion.as_view(), name="AutorNew"),
    path("autor/list", AutorList.as_view(), name="AutorList"),
    path("buscar-autor/", buscar_autor, name="buscar_autor"),
    path("r'(?P<pk>\d+)^$'", AutorDetalle.as_view(), name="AutorDetail"),
    path(r'^borrar/(?P<pk>\d+)$', AutorDelete.as_view(), name="AutorDelete"),
    path(r'^editar/(?P<pk>\d+)$', AutorUpdateView.as_view(), name="AutorUpdate"),
    ##Paginas
    path("pagina-nuevo/", PaginaCreacion.as_view(), name="PaginaNew"),
    path("paginas/list", PaginasList.as_view(), name="PaginasList"),
    path("detalle/<pk>", PaginaDetalle.as_view(), name="PaginaDetail"),
    path("editar/<pk>", PaginaUpdateView.as_view(), name="PaginaUpdate"),
    path("borrar/<pk>", PaginaDelete.as_view(), name="PaginaDelete"),
    path("about/", about_me , name="About"),
]