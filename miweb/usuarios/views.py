from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistroForm, LoginForm

# Create your views here.
class VRegistro(View):

    def get(self,request):
        form=RegistroForm()
        return render(request,'usuarios/registro.html',{'form':form})

    def post(self,request):
        form=RegistroForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            usuario.username = form.cleaned_data['email']  # Utiliza el email como nombre de usuario
            login(request,usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,'usuarios/registro.html',{'form':form})
 


def iniciarSesion(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            contrasena=form.cleaned_data.get("password")
            usuario=authenticate(username=email,password=contrasena)
            if usuario is not None:
                login(request,usuario)
                return redirect('home')
            else:
                messages.error(request,"Usuario no válido")
        else:
            messages.error(request,"Información incorrecta")
    form=LoginForm()
    return render(request,'usuarios/login.html',{'form':form})

def cerrarSesion(request):
    logout(request)
    return redirect('home')