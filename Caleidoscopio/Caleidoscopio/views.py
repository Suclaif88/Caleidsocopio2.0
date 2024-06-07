from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from accounts.models import Usuario

def index(request):
    if request.method == 'POST':
        identificacion = request.POST.get('id')
        contrasena = request.POST.get('pass')
        try:
            usuario = Usuario.objects.get(identificacion=identificacion)
            if check_password(contrasena, usuario.contrasena):
                auth_login(request, usuario)
                return redirect('home')
            else:
                error_message = "Contraseña incorrecta."
                return render(request, 'index.html', {'error_message': error_message, 'show_alert': True})
        except Usuario.DoesNotExist:
            error_message = "No se encontró un usuario con esa identificación."
            return render(request, 'index.html', {'error_message': error_message, 'show_alert': True})
    else:
        return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
