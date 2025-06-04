from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidosSerializers

class PedidosViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidosSerializers