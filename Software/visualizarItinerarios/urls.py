from django.urls import path
from . import views

app_name = 'visualizarItinerarios'
urlpatterns = [
    path('', views.visualizar_itinerarios, name='visualizar_itinerarios'),
    path('detalles/<int:itinerario_id>/', views.detalles_itinerario, name='detalles_itinerario'),
]

