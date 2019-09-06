from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos_list, name='productos_list'),
    path('pedidos_list', views.pedidos_list, name='pedidos_list'),
    path('pedidos/new', views.pedido_new, name='pedido_new'),
]