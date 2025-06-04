from rest_framework.viewsets import ModelViewSet

from core.models import Usuario
from core.serializers import UsuariosSerializers

class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializers