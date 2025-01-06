from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .forms import ActividadForm
from core.models import Itinerario, Actividad

# Ver actividades de itinerario a modificar (sin login_required)
def ver_itinerario(request, itinerario_id):
    itinerario = get_object_or_404(Itinerario, id=itinerario_id)
    actividades = itinerario.actividades.all().order_by('dia','horario')  # Ordena por dia y por horario
    dias_semana = [1, 2, 3, 4, 5, 6, 7]  # Representa los días de la semana de lunes a domingo

    # Se calcula horario inicio-fin y se modifica el formato de hora a 12h
    for actividad in actividades:
        hora_inicio = datetime.combine(datetime.today(), actividad.horario)
        hora_fin = hora_inicio + timedelta(hours=1)
        
        actividad.horario_inicio = hora_inicio.strftime('%I:%M %p').lstrip('0')
        actividad.horario_fin = hora_fin.strftime('%I:%M %p').lstrip('0')
    
    return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'actividades': actividades, 'dias_semana': dias_semana,})


# Agregar actividad (sin login_required)
def agregar_actividad(request, itinerario_id):
    itinerario = get_object_or_404(Itinerario, id=itinerario_id)

    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.itinerario = itinerario
            actividad.save()
            return redirect("ModificarItinerario:ver_itinerario", itinerario_id=itinerario.id)
    else:
        form = ActividadForm()

    return render(request, "agregar_actividad.html", {"form": form, "itinerario": itinerario})


# Modificar actividad (sin login_required)
def modificar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    itinerario_id = actividad.itinerario.id  # Obtiene el itinerario asociado a la actividad

    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect("ModificarItinerario:ver_itinerario", itinerario_id=itinerario_id)  # Cambia a la vista que muestra el itinerario.
    else:
        form = ActividadForm(instance=actividad)

    return render(request, "modificar_actividad.html", {"form": form, "actividad": actividad})


# Eliminar actividad (sin login_required)
def eliminar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    itinerario_id = actividad.itinerario.id  # Guarda el itinerario para redirigir después.
    
    if request.method == "POST":
        actividad.delete()
        return redirect("ModificarItinerario:ver_itinerario", itinerario_id=itinerario_id)  # Cambia a la vista que muestra el itinerario.
    
    return render(request, "eliminar_actividad.html", {"actividad": actividad})
