from django.contrib import admin
from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path("", indexx, name="#"),
    path("suplementos", suplementos, name="suplementos"),
    path("formulario/", form1, name="formulario"),
    path("dnibusqueda/", busquedaDNI, name="dni"),
    path("buscar/", buscar),
]
