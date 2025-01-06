from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
import json
from .models import Viajero, Destino, Itinerario, Actividad


def visualizar_itinerarios(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtiene el objeto Viajero relacionado con el usuario activo
        viajero = request.user.viajero
        # Filtra los itinerarios por el viajero actual
        itinerarios = Itinerario.objects.filter(viajero=viajero)
    else:
        # Si el usuario no está autenticado, no muestra ningún itinerario
        itinerarios = Itinerario.objects.none()

    return render(request, 'visualizar_itinerarios.html', {'itinerarios': itinerarios})

def detalles_itinerario(request, itinerario_id):
    itinerario = get_object_or_404(Itinerario, id=itinerario_id)
    actividades = itinerario.actividades.all().order_by('dia','horario')  # Ordena por dia y por horario
    dias_semana = [1, 2, 3, 4, 5, 6, 7]  # Representa los días de la semana de lunes a domingo

    # Se calcula horario inicio-fin y se modifica el formato de hora a 12h
    for actividad in actividades:
        hora_inicio = datetime.combine(datetime.today(), actividad.horario)
        hora_fin = hora_inicio + timedelta(hours=1)
        
        actividad.horario_inicio = hora_inicio.strftime('%I:%M %p').lstrip('0')
        actividad.horario_fin = hora_fin.strftime('%I:%M %p').lstrip('0')
    
    return render(request, 'detalles_itinerario.html', {'itinerario': itinerario, 'actividades': actividades, 'dias_semana': dias_semana,})




