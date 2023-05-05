from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import (
    AcessorioViewSet,
    MarcaViewSet,
    CategoriaViewSet,
    CorViewSet,
    VeiculoViewSet,
)

router = DefaultRouter()
router.register(r"acessorio", AcessorioViewSet)
router.register(r"marca", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"veiculo", VeiculoViewSet)
router.register(r"cor", CorViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
