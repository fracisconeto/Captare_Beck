from rest_framework.serializers import ModelSerializer

from core.models import Produto

class ProdutoSerializers(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"