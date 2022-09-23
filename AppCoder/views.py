from django.shortcuts import render
from AppCoder.models import *
from django.template import Template, Context
from django.http import HttpResponse
from datetime import datetime
from django.db import models
from AppCoder.forms import *
# Create your views here.

def indexx(request):

    return render(request, "AppCoder/index.html")

def busquedaDNI(request):
    
    return render(request, "AppCoder/DNI.html")

def buscar(request):
    if request.GET["dni"]:

        busqueda = request.GET["dni"]
        pepino = dni1.objects.filter(DNI__icontains=busqueda)
        return render(request, "AppCoder/resultados.html", {"pepino":pepino, "busqueda":busqueda})
    else:
        mensaje = "No existe correlacion"
    return HttpResponse(mensaje)

def suplementos(request):
    
    suplement = suplementos1.objects.get(id=1)
    suplement_ala = suplement.alanina
    suplement_crea = suplement.creatina
    suplement_prote = suplement.proteina
    
    suplementoss = {"alanina":suplement_ala, "creatina":suplement_crea, "proteina": suplement_prote}
    
    return render(request, "AppCoder/suplementos.html", {"suplementos":suplementoss})
        
def form1(request):
    
    if request.method=="POST":
        
        formulario1 = Formulario(request.POST)
        
        if formulario1.is_valid:
            
            info = formulario1
            
            formF = index(correo=info["correo"], nombre=info["nombre"], DNI=info["DNI"])
    
            formF.save()
        
            return render(request, "AppCoder/form1.html")
        
    else:
        formulario1 = Formulario()
    return render(request, "AppCoder/form1.html", {"form1":formulario1})
        
    