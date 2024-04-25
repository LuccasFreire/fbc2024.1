from django.contrib import admin
from .models import Produtos, Categorias
# username: admin 
# password: admin

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('sessao', 'produto', 'custo', 'quantidade', 'especificacoes_tecnicas', 'motivo', 'categoria')

admin.site.register(Produtos, ProdutosAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'descricao')

admin.site.register(Categorias, CategoriasAdmin)