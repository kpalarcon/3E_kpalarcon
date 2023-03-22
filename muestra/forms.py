from django import forms
from django.forms import Form
from .models import Equipo, Trofeo, Torneo

########################################################################################################################

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombreequipo']


class BuscarEquipoForm(Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={
        'placeholder': 'Seleccione una nota',
        'type': 'date', 'size': 30}))
    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={
        'placeholder': 'Seleccione una fecha', 'type': 'date', 'size': 30}))

########################################################################################################################

class TrofeoForm(forms.ModelForm):
    class Meta:
        model = Trofeo
        fields = ['nombretrofeo', 'tipo']


class BuscarTrofeoForm(Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={
        'placeholder': 'Seleccione una nota',
        'type': 'date', 'size': 30}))
    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={
        'placeholder': 'Seleccione una fecha', 'type': 'date', 'size': 30}))

########################################################################################################################

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['equipo', 'trofeo']


class BuscarTorneoForm(Form):
    # nombre = forms.CharField(max_length=200)
    equipo = forms.CharField(max_length=255)
    trofeo = forms.CharField(max_length=255)
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={
        'placeholder': 'Seleccione un trofeo',
        'type': 'date', 'size': 30}))
    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={
        'placeholder': 'Seleccione una fecha', 'type': 'date', 'size': 30}))

########################################################################################################################

class PalabraForm(forms.Form):
    palabra = forms.CharField(max_length=255)

###########################