from django.shortcuts import render
from django.utils import timezone
from comidas.models import Productos
from comidas.models import Participantes
from comidas.models import Pedido
from comidas.forms import CrearPedidos
from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Max

# Crear vista para ingresar al sistema
def ingresar(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        # Añadimos los datos recibidos al formulario
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            clave = formulario.cleaned_data['password']
            # Verificamos las credenciales del usuario
            usr = authenticate(usarname=usuario, password=clave)
            return redirect('pedidos_list')
   
    return render(request, 'pedidos/ingresar.html', {'formulario':formulario})

# Crear vista de cerrar sesión
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('ingresar')

# Crear  vista de lista de productos.
def productos_list(request):
    productos = Productos.objects.order_by('name_prod')
    return render(request, 'productos/productos_list.html', {'productos': productos})

# Crear  vista de lista de pedidos.
def pedidos_list(request):
    pedidos = Pedido.objects.order_by('participante')
    return render(request, 'pedidos/pedidos_list.html', {'pedidos': pedidos})

# Crear vista de crear un pedido.
def pedido_new(request):

    # condicion para crear formulario vacio
    if request.method == "POST":
        form = CrearPedidos(request.POST)
        # condicion para validar formulario
        if form.is_valid():
            cpedido = form.save(commit=False)
            cpedido.auth = request.user
            cpedido.published_date = timezone.now()
            cpedido.product = form.cleaned_data['product']
            cpedido.cantidadp = form.cleaned_data['cantidadp']
            # producto = Productos.objects.values('cantidad')
            # cpedido.cantidadp = F(cantidad) - F(cpedido.cantidadp)
            # producto.save()
            # cantidadp.save()
            cpedido.save()
            return redirect('productos_list')
    else:
        form = CrearPedidos()

    return render(request, 'pedidos/add.html', {'form': form})

# Crear vista del miembro del equipo que consume mas
def come_part(request):
    # se muestra los valores de la relacion participantes pedido se lo anota y se suma la cantidad de productos que ha consumido se ordena por la suma y se obtiene el primero
    comidas = Pedido.objects.values('participante__first_name').annotate(sum=Sum('cantidadp')).order_by('-sum').first()
    return render(request, 'pedidos/come_part.html', {'comidas': comidas})

# Crear vista del miembro del equipo que consume mas
def come_prod(request):
    # se muestra los valores de la relacion productos pedido se lo anota y se suma la cantidad de productos consumidos y luego se muestra el que mas se consumio
    producto = Pedido.objects.values('product__name_prod').annotate(sum=Sum('cantidadp')).order_by('-sum').first()
    return render(request, 'pedidos/come_prod.html', {'producto': producto})



