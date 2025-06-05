from django.db import models
from cliente.models import Cliente
from endereco.models import Endereco
from tecnico.models import Tecnico
from tipoDeServico.models import TipoDeServico
from servicos.models import Servico

# Create your models here.

class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    tipos_servicos = models.ManyToManyField(TipoDeServico)

    data_abertura = models.DateField(auto_now_add=True)
    data_fechamento = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('aberta', 'Aberta'),
            ('em_andamento', 'Em Andamento'),
            ('finalizada', 'Finalizada'),
            ('cancelada', 'Cancelada'),
        ],
        default='aberta'
    )

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
        ordering = ['id']

    def __str__(self):
        return f'Ordem {self.id} - Cliente: {self.cliente.nome}'
