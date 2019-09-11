from django.forms import ModelForm
from .models import Pedido
from django import forms

class CrearPedidos(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['participante','product', 'cantidadp']

