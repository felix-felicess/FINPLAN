from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=10,
        choices=[('receita', 'Receita'), ('despesa', 'Despesa')]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"{self.nome} ({self.tipo})"

class Transacao(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class RelatorioMensal(models.Model):
    mes = models.IntegerField()
    ano = models.IntegerField()
    total_receita = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_despesa = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
