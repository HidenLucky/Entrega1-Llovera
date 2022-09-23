from django.db import models

class index(models.Model):
    
    correo = models.EmailField(max_length=60)
    nombre = models.CharField(max_length=30)
    DNI = models.CharField(max_length=10)

class dni1(models.Model):
    DNI = models.CharField(max_length=10)
    Apellido = models.CharField(max_length=30)



class suplementos1(models.Model):
    creatina = models.URLField(max_length=1000)
    alanina = models.URLField(max_length=1000)
    proteina = models.URLField(max_length=1000)
    