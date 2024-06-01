from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from accounts.models import Usuario

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        identificacion = request.POST.get('id')
        contrasena = request.POST.get('pass')
        try:
            usuario = Usuario.objects.get(identificacion=identificacion)
            if usuario.contrasena == contrasena:
                auth_login(request, usuario)
                if usuario.rol == 1:
                    return redirect('pagina_principal_admin')
                elif usuario.rol == 2:
                    return redirect('pagina_principal_gerente')
                elif usuario.rol == 3:
                    return redirect('DC')
                elif usuario.rol == 4:
                    return redirect('pagina')
                elif usuario.rol == 5:
                    return redirect('RE')
                else:
                    return redirect('index,html')
            else:
                error_message = "Contraseña incorrecta."
                return render(request, 'index.html', {'error_message': error_message, 'show_alert': True})
        except Usuario.DoesNotExist:
            error_message = "No se encontró un usuario con esa identificación."
            return render(request, 'index.html', {'error_message': error_message, 'show_alert': True})
    else:
        return render(request, 'index.html')