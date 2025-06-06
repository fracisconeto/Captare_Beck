from rest_framework.viewsets import ModelViewSet

from core.models import Iten
from core.serializers import ItenSerializer

class ItenViewSet(ModelViewSet):
    queryset = Iten.objects.all()
    serializer_class = ItenSerializer