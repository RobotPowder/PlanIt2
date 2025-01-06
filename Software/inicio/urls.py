from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
   path('inicio/', views.inicio, name='inicio'),
]


