# Generated by Django 4.2.9 on 2024-02-17 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_buku_pendata'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
