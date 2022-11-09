from django.test import TestCase
from AppBlog.models import Autor, User

# Create your tests here.

class ViewTestCase(TestCase):
    
    def test_crear_autor1(self):
        autor = Autor.objects.create(nombre="Juan", apellido="Perez", profesion="Profesional")
        todos_los_autores = Autor.objects.all()

        assert len(todos_los_autores) == 1
        assert todos_los_autores[0].nombre == "Juan"
        assert todos_los_autores[0].apellido == "Perez"
        assert todos_los_autores[0].profesion == "Profesional"
    
    def test_crear_autor2(self):
    
        autor = Autor.objects.create(nombre="Juan", apellido="Perez", profesion="Profesional")
        autor = Autor.objects.create(nombre="Stanley", apellido="Kubrick", profesion="Director")
        autor = Autor.objects.create(nombre="Terry", apellido="Pratchett", profesion="Escritor")
        todos_los_autores = Autor.objects.all()
        
        assert len(todos_los_autores) == 3
        assert todos_los_autores[0].nombre == "Juan"
        assert todos_los_autores[0].apellido == "Perez"
        assert todos_los_autores[0].profesion == "Profesional"
        assert todos_los_autores[1].nombre == "Stanley"
        assert todos_los_autores[1].apellido == "Kubrick"
        assert todos_los_autores[1].profesion == "Director"
        assert todos_los_autores[2].nombre == "Terry"
        assert todos_los_autores[2].apellido == "Pratchett"
        assert todos_los_autores[2].profesion == "Escritor"

    def test_crear_usuario(self):
        usuario = User.objects.create(email="prueba@prueba.com", first_name="John", last_name="Doe")
        todos_los_usuarios = User.objects.all()
        
        assert len(todos_los_usuarios) == 1
        assert todos_los_usuarios[0].email == "prueba@prueba.com"
        assert todos_los_usuarios[0].first_name == "John"
        assert todos_los_usuarios[0].last_name == "Doe"
        

