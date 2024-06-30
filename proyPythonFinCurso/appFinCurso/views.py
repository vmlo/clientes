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
        resum=""
    if foto is None:
        foto=""
    try:
        autor=Autor()
        res=autor.insautor(nom,ape,resum,foto)
        context={
            'res':res
        }
        return render(request,'autor/altaAutor.html',context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "autor/altaAutor.html", contexto)