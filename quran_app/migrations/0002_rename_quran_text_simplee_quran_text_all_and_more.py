# Generated by Django 4.0.5 on 2023-04-07 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quran_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quran_text_simplee',
            new_name='Quran_text_all',
        ),
        migrations.RenameModel(
            old_name='Quran_text_alll',
            new_name='Quran_text_simple',
        ),
    ]
