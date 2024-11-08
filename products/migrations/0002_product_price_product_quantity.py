# Generated by Django 5.0.7 on 2024-08-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
