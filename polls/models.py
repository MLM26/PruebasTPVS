from django.db import models
from django.utils import timezone

class Post(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre

class CargarArchivo(models.Model):
    file = models.FileField()
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre
