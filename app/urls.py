from django.contrib import admin
from django.urls import include, path
from core.views.categoria import CategoriaViewSet
from core.views.endereco import EnderecoViewSet
from core.views.pedido import PedidosViewSet
from core.views.usuario import UsuariosViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'usuarios', UsuariosViewSet, basename='usuarios')
router.register(r'pedidos', PedidosViewSet, basename='pedidos')
router.register(r'endereços',EnderecoViewSet, basename='endereços')
router.register(r'categorias', CategoriaViewSet, basename='categorias')


urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
