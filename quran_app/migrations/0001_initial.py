# Generated by Django 4.0.5 on 2023-04-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quran_text_alll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quran_text_simplee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        # Add a RunSQL operation to create the FULLTEXT index
         # Create a FULLTEXT index on the 'text' column
        migrations.RunSQL(
            sql='CREATE FULLTEXT INDEX text_index ON quran_app_quran_text_alll (text)',
            reverse_sql='DROP INDEX text_index ON quran_app_quran_text_alll',
        ),
        migrations.RunSQL(
            sql='CREATE FULLTEXT INDEX text_index ON quran_app_quran_text_simplee (text)',
            reverse_sql='DROP INDEX text_index ON quran_app_quran_text_simplee',
        ),
    ]
