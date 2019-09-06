from django.db import models
from django.utils import timezone

# Modelo Participantes
class Participantes(models.Model):
    id_part = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.ForeignKey('Productos', on_delete=models.CASCADE)

    # función guardar participante
    def guardar_part(self):
        self.save()

    def __str__(self):
        return self.first_name

# Modelo Productos
class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    name_prod = models.CharField(max_length=70)
    desc_prod = models.CharField(max_length=250)
    cantidad = models.PositiveIntegerField()
    expira_date = models.DateTimeField(default=timezone.now)
    
    def guardar_prod(self):
        self.save()

    def __str__(self):
        return self.name_prod

# Modelo Pedidos
class Pedido(models.Model):
    id_ped = models.AutoField(primary_key=True)
    first_name = models.ForeignKey('Participantes', on_delete=models.CASCADE)
    product = models.ForeignKey('Productos', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField() 
    # se refiere a la cantidad que cada integrante del equipo se quiere comer de cada producto
    published_date = models.DateTimeField(
            blank=True, null=True)

    def guardar_ped(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return '%s %s' % (self.id_ped,'Pedido')