from django.shortcuts import render
from rest_framework import viewsets
from .models import OrdemServico
from .serializer import OrdemServicoSerializer

# Create your views here.

class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')
