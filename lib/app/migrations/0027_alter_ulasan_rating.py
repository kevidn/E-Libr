# Generated by Django 4.2.9 on 2024-02-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_ulasan_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ulasan',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
