from django.shortcuts import render
from rest_framework import viewsets
from .models import OrdemServicoItem
from .serializer import OrdemServicoItemSerializer

# Create your views here.

class OrdemServicoItemViewSet(viewsets.ModelViewSet):
    queryset = OrdemServicoItem.objects.all()
    serializer_class = OrdemServicoItemSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')
