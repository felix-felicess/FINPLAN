from rest_framework import serializers
from financas import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
      model = models.Categoria
      fields = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transacao
        fields = '__all__'

class RelatorioMensalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RelatorioMensal
        fields = '__all__'
