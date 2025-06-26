from django.shortcuts import render
from .models import Servico
from rest_framework import viewsets
from .serializers import ServicoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao', 'preco', 'tipo_de_servico']