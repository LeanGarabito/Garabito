from django.db import models

# Create your models here.

class Auto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    kilometros = models.PositiveIntegerField()
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_autos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.marca} {self.modelo} {self.kilometros} {self.año} {self.precio}"
    