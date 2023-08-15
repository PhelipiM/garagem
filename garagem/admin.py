from django.contrib import admin

from .models import Marca, Categoria, Cor, Veiculo, acessorio

admin.site.register(Marca)

admin.site.register(Categoria)

admin.site.register(acessorio)

admin.site.register(Cor)

admin.site.register(Veiculo)
