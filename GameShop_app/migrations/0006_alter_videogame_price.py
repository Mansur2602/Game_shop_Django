# Generated by Django 5.1.6 on 2025-03-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameShop_app', '0005_rename_developers_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена'),
        ),
    ]
