# Generated by Django 4.2.9 on 2024-02-17 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_pinjam_ket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koleksi',
            old_name='bukus',
            new_name='buku',
        ),
    ]
