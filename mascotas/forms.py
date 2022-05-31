from django import forms

class MascotaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    tipo = forms.CharField(label="Tipo de Animal", max_length=100)
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    edad = forms.IntegerField(label="Edad")
    peso = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "4.6 Kg"}))


class ActualizarMascotaForm(MascotaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarMascotasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")