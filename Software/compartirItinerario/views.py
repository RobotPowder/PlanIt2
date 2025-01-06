# compartirItinerario/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Viajero, Itinerario, ItinerarioCompartido

def compartir_itinerario(request, correo_viajero, itinerario_id=None):
    try:
        viajero = Viajero.objects.get(correo=correo_viajero)
    except Viajero.DoesNotExist:
        messages.error(request, "El viajero no existe.")
        return render(request, 'compartir.html', {'itinerarios': []})

    if request.method == "GET":
        # Si es una solicitud GET, mostrar todos los itinerarios del viajero
        itinerarios = Itinerario.objects.filter(viajero=viajero)
        return render(request, 'compartir.html', {'itinerarios': itinerarios})

    elif request.method == "POST":
        if not itinerario_id:
            messages.error(request, "No se especificó ningún itinerario para compartir.")
            return redirect('compartir_itinerario', correo_viajero=correo_viajero)

        correo_receptor = request.POST.get('correo_destinatario')

        try:
            # Obtener el itinerario por ID
            itinerario = Itinerario.objects.get(id=itinerario_id, viajero=viajero)

            # Crear una copia del itinerario en ItinerarioCompartido
            ItinerarioCompartido.compartir_itinerario(
                itinerario=itinerario,
                correo_emisor=correo_viajero,
                correo_receptor=correo_receptor
            )

            messages.success(request, f"El itinerario '{itinerario.nombre}' se ha compartido con {correo_receptor}.")
        except Itinerario.DoesNotExist:
            messages.error(request, "El itinerario no existe.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {str(e)}")

        return redirect('compartirItinerario:compartir_itinerario', correo_viajero=correo_viajero, itinerario_id=itinerario_id)

