from django.db import models

from garagem.models import Cor, Categoria, Marca, Acessorio

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(
        default=0,
        null=True,
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.modelo}({self.cor}, {self.marca}, {self.ano})"

    class Meta:
        verbose_name = "Veículo"