# Generated by Django 5.1.6 on 2025-03-05 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameShop_app', '0003_developers_videogame_developers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='developers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GameShop_app.developers', verbose_name='Разработчики'),
        ),
    ]
