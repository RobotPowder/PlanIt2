# Generated by Django 3.2.12 on 2024-12-31 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crearItinerario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='itinerario',
        ),
        migrations.DeleteModel(
            name='Destino',
        ),
        migrations.RemoveField(
            model_name='itinerario',
            name='viajero',
        ),
        migrations.RemoveField(
            model_name='itinerariocompartido',
            name='itinerario',
        ),
        migrations.DeleteModel(
            name='Viajero',
        ),
        migrations.DeleteModel(
            name='Actividad',
        ),
        migrations.DeleteModel(
            name='Itinerario',
        ),
        migrations.DeleteModel(
            name='ItinerarioCompartido',
        ),
    ]
