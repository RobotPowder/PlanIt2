from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Viajero


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validar que las contraseñas coincidan
        if password1 != password2:
            return render(request, 'signup.html', {
                'error': 'Las contraseñas no coinciden.',
            })

        # Validar si el correo ya existe
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {
                'error': 'Este correo ya está registrado.',
            })

        # Crear el usuario si todo está bien
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password1)  # Guardar la contraseña encriptada
        )

        # Crear un Viajero y asociarlo al User
        viajero = Viajero.objects.create(
            nombre=username,
            correo=email,
            contraseña=make_password(password1),  # Guardar la contraseña encriptada
            user=user  # Asociamos el User con el Viajero
        )

        login(request, user)  # Inicia sesión automáticamente
        return redirect('inicio:inicio')  # REDIRIGIR A LA PÁGINA PRINCIPAL

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Usar authenticate de Django para verificar las credenciales
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si el usuario es encontrado y las credenciales son correctas
            login(request, user)
            return redirect('inicio:inicio')  # Redirigir a la página principal
        else:
            # Si las credenciales son incorrectas
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta nuevamente.')

    return render(request, 'login.html')  # Renderizar el formulario de login

