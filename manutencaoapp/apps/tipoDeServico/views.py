from django.shortcuts import render
from .models import TipoDeServico
from rest_framework import viewsets
from .serializer import TipoDeServicoSerializer

# Create your views here.

class TipoDeServicoViewSet(viewsets.ModelViewSet):
    queryset = TipoDeServico.objects.all()
    serializer_class = TipoDeServicoSerializer
