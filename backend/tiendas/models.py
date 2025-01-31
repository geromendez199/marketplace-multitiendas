# tiendas/models.py
from django.db import models

class Tienda(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    propietario = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
