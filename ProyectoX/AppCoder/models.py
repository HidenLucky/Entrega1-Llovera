from django.db import models

class index(models.Model):
    
    correo = models.EmailField()
    password = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    DNI = models.IntegerField(help_text="DNI o Pasaporte")

class main(models.Model):

    rutina_hombro = models.CharField(max_length=6)
    rutina_pecho = models.CharField(max_length=5)
    rutina_triceps = models.CharField(max_length=7)
    rutina_espalda = models.CharField(max_length=7)
    rutina_biceps = models.CharField(max_length=6)
    rutina_piernas = models.CharField(max_length=7)
    