from .models import TipoDeServico
from rest_framework import serializers

class TipoDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeServico
        fields = '__all__'
        read_only_fields = ['id']