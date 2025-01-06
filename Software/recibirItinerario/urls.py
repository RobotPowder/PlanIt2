from django.urls import path
from . import views

app_name = 'recibirItinerario'

urlpatterns = [
    path('recibir/<str:correo_viajero>/', views.recibir_itinerario, name='recibir_itinerario'),
]
