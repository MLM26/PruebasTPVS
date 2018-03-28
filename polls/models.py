from django.db import models
from django.utils import timezone

"""
class Trader(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
"""
class CargarArchivo(models.Model):
    nombre = models.CharField(max_length = 50)
    file = models.FileField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("editar")
