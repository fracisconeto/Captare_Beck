from rest_framework.serializers import ModelSerializer

from core.models import Iten

class ItenSerializer(ModelSerializer):
    class Meta:
        model = Iten
        fields = "__all__"