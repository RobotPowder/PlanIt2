from django.urls import path
from . import views

app_name = 'EliminarItinerario'

urlpatterns = [
    path('<int:itinerario_id>/', views.eliminar_itinerario, name='eliminar_itinerario'),
]
