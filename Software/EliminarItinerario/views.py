from django.shortcuts import render, get_object_or_404, redirect
from core.models import Itinerario, Viajero
from django.http import HttpResponseForbidden

def eliminar_itinerario(request, itinerario_id):
    itinerario = get_object_or_404(Itinerario, id=itinerario_id)  # Asegúrate de que esta línea no falle
    if request.method == "POST":
        itinerario.delete()
        return redirect('visualizarItinerarios:visualizar_itinerarios')  # Cambia por la URL correcta para redirigir después de eliminar
    return render(request, 'eliminar_itinerario.html', {'itinerario': itinerario})
