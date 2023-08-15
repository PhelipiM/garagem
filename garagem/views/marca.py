from django.shortcuts import render

from garagem.models import Marca

from rest_framework.viewsets import ModelViewSet

from garagem.serializers import (
    MarcaSerializer,

)

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer