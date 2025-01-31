from django.shortcuts import render
from .models import Tienda

def lista_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas/lista_tiendas.html', {'tiendas': tiendas})
