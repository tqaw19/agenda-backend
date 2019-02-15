from rest_framework import serializers
from .models import Usuario
 
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'telefono', 'dni')

    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    telefono = serializers.CharField()
    dni = serializers.CharField()
 
    def create(self, validated_data):
        """
        Create and return a new `Usuario` instance, given the validated data.
        """
        return Usuario.objects.create(**validated_data)
 
    def update(self, instance, validated_data):
        """
        Update and return an existing `Usuario` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.dni = validated_data.get('dni', instance.dni)        
        instance.save()
        return instance

    