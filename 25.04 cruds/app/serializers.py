from rest_framework import serializers
from .models import Produtos, Categorias, Orcamento, Sessao

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamento
        fields = '__all__'

class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessao
        fields = '__all__'