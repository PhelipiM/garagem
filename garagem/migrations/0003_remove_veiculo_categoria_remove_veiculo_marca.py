# Generated by Django 4.2.4 on 2023-08-22 17:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_veiculo_foto"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="veiculo",
            name="categoria",
        ),
        migrations.RemoveField(
            model_name="veiculo",
            name="marca",
        ),
    ]
