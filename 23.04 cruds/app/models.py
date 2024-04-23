from django.db import models

class Categorias(models.Model):
    categoria = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def str(self):
        return self.categoria

class Produtos(models.Model):
    produto = models.CharField(max_length=255)
    custo = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    especificacoestecnicas = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def str(self):
        return self.produto