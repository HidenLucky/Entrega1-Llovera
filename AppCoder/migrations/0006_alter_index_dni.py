# Generated by Django 4.1.1 on 2022-09-23 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_alter_index_dni_alter_index_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='DNI',
            field=models.IntegerField(max_length=10),
        ),
    ]
