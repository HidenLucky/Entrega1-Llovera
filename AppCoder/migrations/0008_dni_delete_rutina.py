# Generated by Django 4.1.1 on 2022-09-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_alter_index_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='rutina',
        ),
    ]
