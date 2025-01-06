from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Viajero, Destino, Itinerario, Actividad
from datetime import datetime, timedelta

def crear_itinerario(request):
    # Mapeo de los días con sus respectivos números
    dias = {
        'Lunes': 1,
        'Martes': 2,
        'Miércoles': 3,
        'Jueves': 4,
        'Viernes': 5,
        'Sábado': 6,
        'Domingo': 7,
    }
    destinos = Destino.objects.all()

    # Verificar si el usuario está autenticado
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para crear un itinerario.")
        return redirect('LoginSesion:login')

    # Obtener el viajero asociado al usuario autenticado
    viajero = get_object_or_404(Viajero, user=request.user)

    if request.method == 'POST':
        # Recoger los datos del formulario
        nombre = request.POST['nombre']
        fecha = request.POST['fecha']
        fecha_itinerario = datetime.strptime(fecha, '%Y-%m-%d')  # Convertir la fecha a un objeto datetime
        hoy = datetime.now()  # Obtener la fecha actual

        # Validar que la fecha no sea en el pasado
        if fecha_itinerario < hoy:
            messages.error(request, "La fecha del itinerario no puede ser en el pasado.")
            return redirect('crearItinerario:crearItinerario')  # O la ruta correspondiente

        actividades = []

        # Recoger actividades por día
        for dia, dia_id in dias.items():
            horarios_seleccionados = request.POST.getlist(f'horario_{dia_id}[]')
            actividades_dia_desc = request.POST.getlist(f'actividad_{dia_id}[]')
            destinos_seleccionados = request.POST.getlist(f'destino_{dia_id}[]')  # Destinos para cada actividad

            # Si hay actividades para el día, se procesan
            for horario, actividad, destino_id in zip(horarios_seleccionados, actividades_dia_desc, destinos_seleccionados):
                if actividad.strip():
                    destino = Destino.objects.get(id=destino_id)
                    actividades.append({
                        'dia': dia,
                        'horario': horario,
                        'actividad': actividad,
                        'destino': destino,
                    })

        # Crear el itinerario y asociarlo al viajero
        itinerario = Itinerario.objects.create(
            nombre=nombre,
            fecha=fecha_itinerario,
            viajero=viajero,
        )

        # Crear las actividades asociadas al itinerario y con su propio destino
        for actividad in actividades:
            Actividad.objects.create(
                itinerario=itinerario,
                nombre=actividad['actividad'],
                horario=actividad['horario'],
                destino=actividad['destino'],  # Asignar el destino específico de la actividad
                dia=dias[actividad['dia']],
            )

        return redirect('inicio:inicio')

    return render(request, 'crear_itinerario.html', {'dias': dias, 'destinos': destinos})
