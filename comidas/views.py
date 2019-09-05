from django.shortcuts import render
from django.utils import timezone
from .models import Productos

# Crear  vista de pedidos.
def productos_list(request):
    productos = Productos.objects.order_by('name_prod')
    return render(request, 'productos/productos_list.html', {'productos': productos})


