from django.db import models
from django.utils import timezone

class Sistema(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion =  models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField( blank=True, null=True)
    identificador = models.CharField(max_length=100)

    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Trader(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha = models.DateTimeField( blank=True, null=True)
    documento = models.CharField(max_length=100)
    identificador = models.CharField(max_length=100)

    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.identificador

class Portafolio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField( blank=True, null=True)
    identificador = models.CharField(max_length=100)

    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Archivo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    ruta = models.FileField()
    fecha = models.DateTimeField( blank=True, null=True)

    def update(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
    """
class Archivo(models.Model):
    nombre = models.CharField(max_length = 50)
    file = models.FileField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar',kwargs={'pk':self.pk})
"""
