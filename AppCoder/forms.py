from django import forms

class Formulario(forms.Form):
    
    correo = forms.EmailField()
    nombre = forms.CharField()
    DNI = forms.CharField() 

