from django.shortcuts import render
from django.utils import timezone
from .models import Productos
from .models import Pedido
from .forms import CrearPedidos
from django.shortcuts import redirect
from django.db.models import Count

# Crear  vista de lista de productos.
def productos_list(request):
    productos = Productos.objects.order_by('name_prod')
    return render(request, 'productos/productos_list.html', {'productos': productos})

# Crear  vista de lista de pedidos.
def pedidos_list(request):
    pedidos = Pedido.objects.order_by('first_name')
    return render(request, 'pedidos/pedidos_list.html', {'pedidos': pedidos})

# Crear vista de crear un pedido.
def pedido_new(request):
    
    # condicion para crear formulario vacio
    if request.method == "POST":
        form = CrearPedidos(request.POST)
        # condicion para verificar si todos los campos del formulario estan vacios
        if form.is_valid():
            cpedido = form.save(commit=False)
            cpedido.author = request.user
            cpedido.published_date = timezone.now()
            cpedido.save()
            return redirect('productos_list')
    else:
        form = CrearPedidos()

    return render(request, 'pedidos/add.html', {'form': form})

# Crear la vista para ver la persona que mas consumio
def part_mascome(request):
    q = Pedidos.objects.annotate(Count('first_name'))