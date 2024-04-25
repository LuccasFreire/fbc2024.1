from django.urls import path
from rest_framework import routers
from .views import ProdutosViewSet, CategoriasViewSet, OrcamentoViewSet, SessaoViewSet
router = routers.DefaultRouter()

router.register(r'produtos', ProdutosViewSet)
router.register(r'categorias', CategoriasViewSet)
router.register(r'orcamentos', OrcamentoViewSet)
router.register(r'sessoes', SessaoViewSet)
urlpatterns = router.urls