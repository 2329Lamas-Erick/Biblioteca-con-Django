from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationFrom

def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': CustomUserCreationFrom})
    
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Autenticacion manuel del usuario creado
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, user)

            # Redireccion a la pagina principal
            return redirect('home')
        else:
            # Hubo errores en el formulario
            return render(request, 'registration/register.html', {"form": form})
        
# Aplicacion
@login_required
def home(request):
    context = {}

    return render(request, 'home/index.html', context)