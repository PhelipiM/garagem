from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca, Veiculo, Acessorio, Categoria, Cor
from garagem.serializers import MarcaSerializer, CategoriaSerializer, CorSerializer, VeiculoSerializer, AcessorioSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
