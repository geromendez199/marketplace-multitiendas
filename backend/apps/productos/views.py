from django.shortcuts import render
from .models import Producto

def lista_productos(request, tienda_id):
    productos = Producto.objects.filter(tienda_id=tienda_id)
    return render(request, 'productos/lista_productos.html', {'productos': productos})
