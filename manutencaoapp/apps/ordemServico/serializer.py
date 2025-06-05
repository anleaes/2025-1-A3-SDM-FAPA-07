from .models import OrdemServico
from rest_framework import serializers

class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = '__all__'
        read_only_fields = ['id']