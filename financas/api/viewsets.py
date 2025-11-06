from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from financas import models
from financas.api import serializers

class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Transacao.objects.all()
    serializer_class = serializers.TransacaoSerializer

class RelatorioMensalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.RelatorioMensal.objects.all()
    serializer_class = serializers.RelatorioMensalSerializer
