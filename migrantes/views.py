from django.shortcuts import render, redirect
from .formularios import Formulario_Migrante
from .models import migrantes
# Create your views here.

def tabla_migrantes(request):
    contexto = {'tabla_migrantes':migrantes.objects.all()}
    return render(request,"registro_migrantes/tabla_migrantes.html", contexto)

def formulario_migrantes(request,id=0):
    if(request.method=="GET"):
        if(id==0):
            formulario = Formulario_Migrante()
        else:
            migrante = migrantes.objects.get(pk=id)
            formulario = Formulario_Migrante(instance=migrante)

        return render(request,"registro_migrantes/formulario_migrantes.html",{'formulario':formulario})
    else:
        if(id==0):
            formulario = Formulario_Migrante(request.POST)
        else:
            migrante = migrantes.objects.get(pk=id) 
            formulario = Formulario_Migrante(request.POST,instance=migrante)

        if(formulario.is_valid()):
            print(request.POST)
            formulario.save()
            return redirect('/migrantes/tablaMigrantes')
        else:
            print("No valido")
            return redirect('/migrantes')
def eliminar_migrantes(request,id):
    migrante = migrantes.objects.get(pk=id) 
    migrante.delete()
    return redirect('/migrantes/tablaMigrantes')
     


