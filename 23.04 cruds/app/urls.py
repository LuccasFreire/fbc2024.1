from django.urls import path
from rest_framework import routers
from .views import ProdutosViewSet, CategoriasViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutosViewSet)
router.register(r'categorias', CategoriasViewSet)
urlpatterns = router.urls