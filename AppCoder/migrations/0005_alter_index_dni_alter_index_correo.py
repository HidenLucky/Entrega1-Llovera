# Generated by Django 4.1.1 on 2022-09-23 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alter_suplementos1_alanina_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='DNI',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='index',
            name='correo',
            field=models.EmailField(max_length=60),
        ),
    ]