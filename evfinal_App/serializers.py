from rest_framework import serializers
from evfinal_App.models import Instituciones,Inscritos

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = '__all__'

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'