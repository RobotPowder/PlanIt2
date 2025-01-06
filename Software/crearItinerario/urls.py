from django.urls import path
from . import views

app_name = 'crearItinerario'

urlpatterns = [
    path('', views.crear_itinerario, name='crear_itinerario'),

]

