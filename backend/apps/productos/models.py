# productos/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    en_venta = models.BooleanField(default=False)
    en_alquiler = models.BooleanField(default=False)
    tienda = models.ForeignKey('tiendas.Tienda', related_name='productos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
