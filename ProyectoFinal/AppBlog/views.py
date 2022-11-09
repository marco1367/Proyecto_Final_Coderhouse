from django.shortcuts import render
from AppBlog.forms import UserEditionForm, UserRegisterForm, AvatarForm
from AppBlog.models import Autor, Pagina, Avatar
from django.contrib.auth.models import User

from django.templatetags.static import static

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, 'homepage.html')

class Login(LoginView):
    template_name = "AppBlog/login.html"
    
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                avatarUrl = Avatar.objects.filter(user_id = user.id)[0].imagen.url
                print('avatar', avatarUrl)##-----
                print('userId:', user.id)
                return render(request, 'homepage.html', {'avatarUrl': avatarUrl}) ##Poner luego el avatar
            else:
                return render(request, 'login.html', {'form': form ,'mensaje': "Error. Datos incorrectos"})
        else:
            return render(request, 'login.html', {'form': form ,'mensaje': "Error. Datos incorrectos"})


class Logout(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"

## Editar usuario:
@login_required
def editar_perfil(request):
    user = request.user
    if user.first_name:
        print('user: ', user.username)
    # avatar = Avatar.objects.filter(user=request.user).first()

    if request.method != "POST":
        form = UserEditionForm(initial={
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.save()
            # return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})
            return render(request, "homepage.html")


    contexto = {
    "user": user, 
    "form": form,
    # "avatar": avatar.imagen.url
    }
    return render(request, "editarPerfil.html", contexto)



## Crear usuario:
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            ##agregar avatar por default:
            u = User.objects.get(username= form.cleaned_data["username"])
            avatar = Avatar(user= u, imagen= static('/media/avatarDefault.png') )
            avatar.save()

            avatarUrl =avatar.imagen.url

            return render(request, "homepage.html", {"mensajeRegister": f"Usuario {username_capturado} creado con exito !", 'avatarUrl': avatarUrl})
    else:
        form = UserRegisterForm()
    
    return render(request, "registro.html", {"form": form})

##Agregar avatar a usuario:
# @login_required
# def agregar_avatar(request):
#     if request.method != "POST":
#         form = AvatarForm()
#     else:
#         form = AvatarForm(request.POST, request.FILES)
#         if form.is_valid():
#             Avatar.objects.filter(user=request.user.id).delete()
#             form.save()
#             return render(request, "AppBlog/homepage.html")

#     contexto = {"form": form}
#     return render(request, "AppBlog/avatar_form.html", contexto)

@login_required
def agregar_avatar(request):
    # avatarUrl = Avatar.objects.filter(user = request.user.id)[0].imagen.url

    if request.method == 'POST': # Cunado enviamos el formulario (Es un metodo POST)
       
        miFormulario = AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(id= request.user.id)

            # avatar = Avatar(user= u, imagen= miFormulario.cleaned_data['imagen'])
            # avatar.save()

            avatar = Avatar.objects.filter(user= u)[0]
            avatar.imagen = miFormulario.cleaned_data['imagen']
            print('avatar image:', avatar.imagen.url)##-----
            avatar.save()

            return render(request, "AppBlog/homepage.html", {'avatarUrl': avatar.imagen.url})
    else:

        miFormulario = AvatarForm() # Formulario vacio para construir el html (cunado ingresamos)
        return render(request, "AppBlog/avatar_form.html", {'form': miFormulario})
## --------------------------------------- ##





## Crear autor:
class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    fields = ["nombre", "apellido", "profesion"]
    # success_url = "/blog/autor/list"
    success_url = "/AppBlog/"


##Lista autores:
class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "autor_list.html"

##Buscar autor:
@login_required
def buscar_autor(request):
    if request.method == "GET":
        return render(request, "AppBlog/formulario-de-busqueda-autor.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "AppBlog/resultados-de-la-busqueda.html", context = contexto)


##Detalle autor:
class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "AppBlog/autor_detalle.html"

    
##Borrar autor:
class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/autor/list"

##Ctualizar autor:
class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/autor/list"
    fields = ["nombre", "apellido", "profesion"]


##Crear pagina:
class PaginaCreacion(LoginRequiredMixin, CreateView):
    model = Pagina
    fields = ["autor", "titulo", "subtitulo", "texto", "fecha", "foto"]
    success_url = "/paginas/list"


##Lista paginas:
class PaginasList(LoginRequiredMixin, ListView):
    model = Pagina
    template_name = "paginas_list.html"


class PaginaDetalle(LoginRequiredMixin, DetailView):
    model = Pagina
    template_name = "pagina_detalle.html"


class PaginaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pagina
    success_url = "/AppBlog/paginas/list"
    fields = ["autor", "titulo", "subtitulo", "texto", "fecha", "foto"]


class PaginaDelete(LoginRequiredMixin, DeleteView):
    model = Pagina
    success_url = "/AppBlog/paginas/list"


def about_me(request):
    return render(request, "AppBlog/about.html")
