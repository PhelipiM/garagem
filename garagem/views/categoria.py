from django.shortcuts import render

from garagem.models import Categoria

from rest_framework.viewsets import ModelViewSet

from garagem.serializers import (
    CategoriaSerializer,

)

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer