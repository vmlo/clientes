from django.shortcuts import render
from appFinCurso.models import Autor


def inicio(request):
    return render(request,'index.html')

def altaAutorF(request):
    return render(request,'autor/altaAutor.html')

def altaAutorRes(request):
    nom=request.POST['nombre']
    ape=request.POST['apellidos']
    resum = request.POST['resumen']
    foto = request.POST['foto']
    if resum is None:
        resum="Null"
    if foto is None:
        foto="Null"
    try:
        autor=Autor()
        nd=autor.insautor(nom,ape,resum,foto)
        if nd>0:
            res="Autor dado de alta correctamente"
        else:
            res = "Error: el Autor no ha podido darse de alta"
        context={
            'mensaje':res
        }
        return render(request,'index.html',context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "index.html", contexto)

def autores(request):
    try:
        autor=Autor()
        datos=autor.autores()
        context = {
            'resultado': datos
        }
        return render(request,'autor/autores.html',context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "autor/autores.html", contexto)