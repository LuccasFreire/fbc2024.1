from argparse import Action
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Produtos, Categorias, Sessao, Orcamento
from .serializers import ProdutosSerializer, CategoriasSerializer
from app import models
from rest_framework.decorators import action
from rest_framework.response import Response

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    pagination_class = LimitOffsetPagination

    #@action(detail=False, methods=['get'])
    #def total_cost(self, request):
        #total = Produtos.objects.all().aggregate(total_cost=models.Sum('CUSTO'))['total_cost']
        #return Response({'total_cost': total})

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    pagination_class = LimitOffsetPagination

class OrcamentoViewSet(viewsets.ModelViewSet):
    queryset = Orcamento.objects.all()
    serializer_class = CategoriasSerializer
    pagination_class = LimitOffsetPagination

class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = CategoriasSerializer
    pagination_class = LimitOffsetPagination