from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import Avatar


class UserEditionForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar email", required=False)
    # password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    # password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=30, required=False)
    last_name = forms.CharField(label="Apellido", max_length=30, required=False)
    password1 = None
    password2 = None
    username = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', max_length=30)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ['username', 'password1', 'password2']
        ##Sacar los mensajes de ayuda:
        help_texts = {k:"" for k in fields}



class AvatarForm(forms.Form):
    imagen = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ['user', 'imagen']
