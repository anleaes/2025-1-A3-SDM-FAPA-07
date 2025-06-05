from django.shortcuts import render
from .models import Endereco
from .serializer import EnderecoSerializer

# Create your views here.

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        return self.queryset.order_by('id')
