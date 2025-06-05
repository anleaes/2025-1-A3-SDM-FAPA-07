from django.db import models

# Create your models here.

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    especialidade = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['id']

    def __str__(self):
        return self.nome