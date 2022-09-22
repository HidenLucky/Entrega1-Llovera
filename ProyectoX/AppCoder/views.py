from django.shortcuts import render
from AppCoder.models import *
from django.template import Template, Context
from django.http import HttpResponse
from datetime import datetime
from django.db import models
# Create your views here.

def index(request):

    miHtml = open("C:/Users/Marco/Desktop/MVT/ProyectoX/ProyectoX/plantillas/index.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)

def main(request):
    
    miHtml = open("C:/Users/Marco/Desktop/MVT/ProyectoX/ProyectoX/plantillas/main.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)