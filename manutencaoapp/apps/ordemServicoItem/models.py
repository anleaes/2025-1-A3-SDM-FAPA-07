from django.db import models
from ordemServico.models import OrdemServico
from servicos.models import Servico

# Create your models here.

class OrdemServicoItem(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='itens')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Item da Ordem de Serviço'
        verbose_name_plural = 'Itens da Ordem de Serviço'
        ordering = ['id']

    def __str__(self):
        return f'{self.quantidade}x {self.servico.nome} (OS {self.ordem_servico.id})'