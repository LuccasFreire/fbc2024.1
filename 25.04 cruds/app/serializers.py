from rest_framework import serializers
from .models import Produtos, Categorias

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'