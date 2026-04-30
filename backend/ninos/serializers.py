from rest_framework import serializers
from .models import Nino, Escuela, Tutor

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = ['id', 'nombre', 'turno', 'zona']

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id', 'nombre', 'telefono']

class NinoSerializer(serializers.ModelSerializer):
    escuela = EscuelaSerializer()
    tutor = TutorSerializer()

    class Meta:
        model = Nino
        fields = ['id', 'codigo', 'nombre', 'fecha_nacimiento', 'fecha_registro', 'escuela', 'tutor']
