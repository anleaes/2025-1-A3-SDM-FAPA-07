from django.db import models
from cliente.models import Cliente

# Create your models here.

class Equipamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='equipamentos')
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering = ['id']

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.numero_serie}'
