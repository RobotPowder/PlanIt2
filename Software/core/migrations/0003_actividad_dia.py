# Generated by Django 3.2.12 on 2025-01-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_itinerariocompartido_emisor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='dia',
            field=models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')], null=True),
        ),
    ]