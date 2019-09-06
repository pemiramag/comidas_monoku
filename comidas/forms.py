from django.forms import ModelForm
from .models import Pedido
from django import forms

class CrearPedidos(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['first_name', 'product' , 'cantidad',]

