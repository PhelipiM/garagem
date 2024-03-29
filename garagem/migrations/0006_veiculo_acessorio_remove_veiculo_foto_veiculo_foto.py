# Generated by Django 4.2.4 on 2023-08-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("garagem", "0005_alter_veiculo_modelo"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="acessorio",
            field=models.ManyToManyField(
                related_name="veiculos", to="garagem.acessorio"
            ),
        ),
        migrations.RemoveField(
            model_name="veiculo",
            name="foto",
        ),
        migrations.AddField(
            model_name="veiculo",
            name="foto",
            field=models.ManyToManyField(related_name="+", to="uploader.image"),
        ),
    ]
