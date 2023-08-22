# Generated by Django 4.2.4 on 2023-08-22 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0003_remove_veiculo_categoria_remove_veiculo_marca"),
    ]

    operations = [
        migrations.CreateModel(
            name="Modelo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(default="", max_length=150)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modelos",
                        to="garagem.categoria",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modelos",
                        to="garagem.marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "Modelo",
            },
        ),
    ]