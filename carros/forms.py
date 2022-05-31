from django import forms

class CarroForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    marca = forms.CharField(label="Marca", max_length=100)
    ano_creacion = forms.IntegerField(label="Año de Creacion")
    cap_lts = forms.FloatField(label= "Capacidad de Combustible en Litros", widget=forms.NumberInput(attrs={'placeholder': "45.6 Lts"}))


class ActualizarCarroForm(CarroForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarCarrosForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")