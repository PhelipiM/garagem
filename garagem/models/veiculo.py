from django.db import models
from uploader.models import Image

from garagem.models import Cor, Categoria, Marca, Acessorio, Modelo

class Veiculo(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0,null=True,)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    modelo = models.ForeignKey( Modelo,on_delete=models.PROTECT, related_name="veiculos" )
    foto = models.ForeignKey(Image,related_name="+",on_delete=models.CASCADE,null=True,blank=True, default=None,)

    def __str__(self):
        return f"{self.modelo}({self.cor}, {self.ano})"

    class Meta:
        verbose_name = "Veículo"

