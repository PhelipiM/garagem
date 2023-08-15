from rest_framework.serializers import ModelSerializer

from garagem.models import acessorio

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = acessorio
        fields = "__all__"