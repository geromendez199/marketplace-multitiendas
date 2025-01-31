from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tiendas, name='lista_tiendas'),
]
