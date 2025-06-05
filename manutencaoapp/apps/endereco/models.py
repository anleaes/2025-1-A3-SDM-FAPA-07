from django.db import models
from cliente.models import Cliente

# Create your models here.

class Endereco(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='enderecos'
    )
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['id']

    def __str__(self):
        return f'{self.rua}, {self.cidade} - {self.estado}'
