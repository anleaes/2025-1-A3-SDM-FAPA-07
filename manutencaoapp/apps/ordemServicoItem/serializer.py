from .models import OrdemServicoItem
from rest_framework import serializers

class OrdemServicoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServicoItem
        fields = '__all__'
        read_only_fields = ['id']