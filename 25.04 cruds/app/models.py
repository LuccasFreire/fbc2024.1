from django.db import models

class Categorias(models.Model):
    categoria = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def str(self):
        return self.nome

class Produtos(models.Model):
    sessao = models.CharField(max_length=255)
    produto = models.CharField(max_length=255)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    especificacoes_tecnicas = models.TextField(default='')
    motivo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def str(self):
        return self.produto