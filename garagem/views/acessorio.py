from django.shortcuts import render

from garagem.models import acessorio

from rest_framework.viewsets import ModelViewSet

from garagem.serializers import (
    AcessorioSerializer,

)

class AcessorioViewSet(ModelViewSet):
    queryset = acessorio.objects.all()
    serializer_class = AcessorioSerializer