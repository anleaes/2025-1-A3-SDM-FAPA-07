from django.db import models

# Create your models here.

class TipoDeServico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo de serviço'
        verbose_name_plural = 'Tipos de serviços'
        ordering =['id']

    def __str__(self):
        return self.nome
