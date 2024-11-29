from  django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

class Crear_Sabor_forms(forms.Form):
    nombre = forms.CharField(max_length=30)


class Crear_Cliente_forms(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class Crear_Helado_forms(forms.Form):
    nombre = forms.CharField(max_length=30)
    precio = forms.DecimalField(max_digits=8, decimal_places=2)
    sabor = forms.ModelChoiceField(queryset=Sabor.objects.all())

class Crear_Pedido_forms(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    fecha = forms.DateTimeField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repetir contraseña',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}
              

