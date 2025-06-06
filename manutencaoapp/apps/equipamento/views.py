from django.shortcuts import render
from rest_framework import viewsets
from .models import Equipamento
from .serializer import EquipamentoSerializer

# Create your views here.

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')
