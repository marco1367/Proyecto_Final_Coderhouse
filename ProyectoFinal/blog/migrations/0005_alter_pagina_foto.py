# Generated by Django 4.1.1 on 2022-11-05 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_pagina_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]
