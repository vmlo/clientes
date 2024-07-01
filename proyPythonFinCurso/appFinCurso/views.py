from django.shortcuts import render
from appFinCurso.models import Autor
from appFinCurso.models import Libro
from appFinCurso.models import DatosTipo

def inicio(request):
    return render(request,'index.html')
"""Autores"""
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
        return render(request, "index.html", contexto)

def autor(request):
    try:
        id=int(request.GET['id'])
        autor = Autor()
        datos=autor.autorById(id)
        context={
            'resultado': datos
        }
        return render(request,'autor/autor.html', context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "index.html", contexto)

def delAutor(request):
    try:
        id = int(request.GET['id'])
        autor = Autor()
        datos=autor.delautor(id)
        if datos>0:
            res="Autor dado de alta correctamente"
        else:
            res = "Error: el Autor no ha podido darse de alta"
        context = {
            'mensaje': res
        }
        return render(request, "index.html", context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "index.html", contexto)

def modAutorF(request):
    try:
        id=int(request.GET['id'])
        autor = Autor()
        datos=autor.autorById(id)
        context={
            'resultado': datos
        }
        return render(request, "autor/modAutor.html",context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "index.html", contexto)

def modAutor(request):
    try:
        id=request.POST['id']
        nom = request.POST['nombre']
        ape = request.POST['apellidos']
        resum = request.POST['resumen']
        foto = request.POST['foto']
        if resum is None:
            resum = "Null"
        if foto is None:
            foto = "Null"
        autor = Autor()
        nd = autor.modautor(id,nom, ape, resum, foto)
        if nd > 0:
            res = "Autor modificado correctamente"
        else:
            res = "Error: el Autor no ha podido darse de alta"
        context = {
           'mensaje': res
        }
        return render(request, "index.html",context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "index.html", contexto)

    """Libros"""


def sellibros(request):
    try:
        libro = Libro()
        datoslibro = libro.libros()
        for id,tit,col,num in datoslibro:
            autor=Autor()
            datosAutor=autor.autorByLibro(id)
            genero=DatosTipo()
            datosGen=genero.tipoByLibro(id)
            datos={
                'idlibro':id,
                'titulo':tit,
                'coleccion':col,
                'numCol':num,
                'autores':datosAutor,
                'generos':datosGen
            }
        context = {
            'resultado': datos
        }
        return render(request, 'libros/libros.html', context)
    except Exception as err:
        contexto = {
            'mensaje': err
        }
        return render(request, "index.html", contexto)