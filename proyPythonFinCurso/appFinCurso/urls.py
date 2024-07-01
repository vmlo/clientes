from django.urls import path
from appFinCurso import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('inicio',views.inicio,name='inicio'),
    path('viewAltaAutorF', views.altaAutorF, name='AltaAutorForm'),
    path('altaAutorRes', views.altaAutorRes, name="altaAutorRes"),
    path('viewAutores', views.autores, name='Autores'),
    path('viewAutor', views.autor, name='Autor'),
    path('borrAutor', views.delAutor, name='borrAutor'),
    path('viewModAutor', views.modAutorF, name='viewModAutor'),
    path('modAutorRes', views.modAutor, name='modAutorRes'),
    path('viewTipos', views.listaMaestroTipos,name='maestroDeTipos')
]