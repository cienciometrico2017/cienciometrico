from django import forms
from apps.ponencias.models import Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model= Evento
        fields= [
            'nombre',
            'lugar',
            'fecha',

        ]
        labels={
            'nombre':'Nombre',
            'lugar':'Lugar',
            'fecha':'Fecha',

        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'lugar':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),

        }