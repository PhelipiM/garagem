# Generated by Django 4.1.7 on 2023-03-31 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_veiculo_modelo_alter_veiculo_ano_alter_veiculo_preco'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'Acessório'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name_plural': 'cores'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veículo'},
        ),
    ]
