from rest_framework import serializers
from manada.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut','nombre','gmail','telefono','direccion','usuario']