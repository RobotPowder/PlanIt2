from django import forms
from core.models import Actividad, Destino
from datetime import time

class ActividadForm(forms.ModelForm):
    HORARIOS = [(time(hour=h), f"{h:02d}:00 - {h + 1:02d}:00") for h in range(0, 24)]

    horario = forms.ChoiceField(choices=HORARIOS, label="Horario")
    destino = forms.ModelChoiceField(queryset=Destino.objects.all(), label="Destino", empty_label="Seleccione un destino")

    class Meta:
        model = Actividad
        fields = ["horario", "dia", "nombre", "destino"]  #Formulario donde se ingresan los datos de la actividad

    def clean_horario(self):
        horario = self.cleaned_data["horario"]
        return time.fromisoformat(horario)  # Convierte de string a objeto `time`
