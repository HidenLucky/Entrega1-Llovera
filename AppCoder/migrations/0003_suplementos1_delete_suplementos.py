# Generated by Django 4.1.1 on 2022-09-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_index_rutina_suplementos_delete_familia'),
    ]

    operations = [
        migrations.CreateModel(
            name='suplementos1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatina', models.URLField(max_length=1)),
                ('alanina', models.URLField(max_length=1)),
                ('proteina', models.URLField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='suplementos',
        ),
    ]
