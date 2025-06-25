from django.shortcuts import render
from .models import TipoDeServico
from rest_framework import viewsets
from .serializer import TipoDeServicoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TipoDeServicoViewSet(viewsets.ModelViewSet):
    queryset = TipoDeServico.objects.all()
    serializer_class = TipoDeServicoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
