# Generated by Django 4.2.9 on 2024-02-19 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_ulasan_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='kelompok',
            name='bukus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.buku'),
            preserve_default=False,
        ),
    ]
