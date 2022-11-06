from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Avatar

class ArticuloForm(forms.Form):
    
    titulo = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Titulo del articulo', 'style': 'width: 20vw;'}))
    subtitulo = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Subtitulo', 'style': 'width: 20vw;'}))
    texto = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Ingrese el contenido','style': 'width: 20vw;'}))
    fecha = forms.DateField(input_formats=['%d/%m/%Y','%d-%m-%Y' ],widget=forms.TextInput(attrs={'label':'Fecha de publicacion','placeholder': "01/01/2000", 'style': 'width: 20vw;'}))
    imagen = forms.ImageField()

class AutorForm(forms.Form):
    
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 20vw;'}))
    apellido = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'style': 'width: 20vw;'}))
    profesion = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Profesión', 'style': 'width: 20vw;'}))
    

class UserEditionForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.ModelForm):

    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]

