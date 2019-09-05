from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos_list, name='productos_list'),
]