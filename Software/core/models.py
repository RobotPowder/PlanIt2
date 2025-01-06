from django.db import models
from django.contrib.auth.models import User  # Importar el modelo User de Django

DIA_CHOICES = [
    (1, 'Lunes'),
    (2, 'Martes'),
    (3, 'Miércoles'),
    (4, 'Jueves'),
    (5, 'Viernes'),
    (6, 'Sábado'),
    (7, 'Domingo'),
]

# Modelo Viajero con relación al modelo User
class Viajero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="viajero", null=False)  # Relación con User
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo Itinerario con relación al usuario activo
class Itinerario(models.Model):
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE, related_name="itinerarios")  # Relación con Viajero
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

    @staticmethod
    def solicitar_itinerarios_viajero(viajero_id):
        """Devuelve todos los itinerarios de un viajero por su ID."""
        return Itinerario.objects.filter(viajero_id=viajero_id)

    def __str__(self):
        return self.nombre


class Destino(models.Model):
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.ciudad}, {self.pais}"


class Actividad(models.Model):
    horario = models.TimeField()
    nombre = models.CharField(max_length=100)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="actividades")
    itinerario = models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name="actividades")
    dia = models.IntegerField(choices=DIA_CHOICES, null=True)

    def __str__(self):
        return self.nombre


class ItinerarioCompartido(models.Model):
    itinerario = models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name="itinerario_compartido")
    emisor = models.EmailField()
    receptor = models.EmailField()

    @staticmethod
    def compartir_itinerario(itinerario, correo_emisor, correo_receptor):
        """
        Crea una nueva relación de itinerario compartido.
        """
        return ItinerarioCompartido.objects.create(
            itinerario=itinerario,
            emisor=correo_emisor,
            receptor=correo_receptor
        )

