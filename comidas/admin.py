from django.contrib import admin
from .models import Productos
from .models import Participantes
from .models import Pedido

admin.site.register(Productos)
admin.site.register(Participantes)
admin.site.register(Pedido)