# Generated by Django 4.1.7 on 2023-03-21 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0003_acessorio_cor"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name_plural": "Cores"},
        ),
        migrations.CreateModel(
            name="Veiculo",
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
                (
                    "ano",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=7, null=True
                    ),
                ),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=7, null=True
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="garagem.categoria",
                    ),
                ),
                (
                    "cor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="garagem.cor",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="garagem.marca",
                    ),
                ),
            ],
        ),
    ]
