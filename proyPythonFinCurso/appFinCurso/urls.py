from django.urls import path

from appFinCurso import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('inicio',views.inicio,name='inicio'),
    path('viewAltaAutorF', views.altaAutorF,name='AltaAutorForm'),
    path('altaAutorRes',views.altaAutorRes,name="altaAutorRes")
]