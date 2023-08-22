from django.db import models
from uploader.models import Image

from garagem.models import Cor, Categoria, Marca, Acessorio, Modelo

class Veiculo(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0,null=True,)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    modelo = models.ForeignKey( Modelo,on_delete=models.PROTECT, related_name="veiculos" )
    foto = models.ManyToManyField(Image,related_name="+")
    acessorio = models.ManyToManyField(Acessorio,related_name="veiculos")
    

    def __str__(self):
        return f"{self.modelo}({self.cor}, {self.ano})"

    class Meta:
        verbose_name = "Veículo"

