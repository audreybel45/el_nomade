

# Create your models here.
from django.db import models

class PuntoTuristico(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField()
    hospedajes = models.CharField(max_length=255)
    transporte = models.CharField(max_length=255)
    formas_llegar = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    ubicacion = models.CharField(max_length=255)
