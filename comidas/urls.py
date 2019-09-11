from django.urls import path
from . import views
urlpatterns = [
    path('', views.ingresar, name='ingresar'),
    path('productos_list', views.productos_list, name='productos_list'),
    path('pedidos_list', views.pedidos_list, name='pedidos_list'),
    path('pedidos/new', views.pedido_new, name='pedido_new'),
    path('come_part', views.come_part, name='come_part'),
    path('come_prod', views.come_prod, name='come_prod'),
]