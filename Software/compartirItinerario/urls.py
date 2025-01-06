from django.urls import path
from . import views

app_name = 'compartirItinerario'

urlpatterns = [
    path('compartir/<str:correo_viajero>/<int:itinerario_id>/', views.compartir_itinerario, name='compartir_itinerario'),
]


