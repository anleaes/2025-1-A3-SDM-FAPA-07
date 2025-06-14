from .models import Tecnico
from rest_framework import serializers

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'
        read_only_fields = ['id']