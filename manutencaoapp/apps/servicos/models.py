from django.db import models
from tipoDeServico.models import TipoDeServico

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_de_servico = models.ForeignKey(TipoDeServico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['id']

    def __str__(self):
        return self.nome