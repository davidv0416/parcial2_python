from django import views
from django.urls import URLPattern,path
from . import views
 

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('index',views.index,name="index"),
    path('nombre/<nom>/<int:edad>',views.mostrarnombre,name="imprimenombre"),
    path('info',views.informacion,name="info"),
    path('info2',views.informacion2),
    path('enviar',views.enviar,name="enviar"),
    path('crearAnimal',views.crearAnimal,name="crearAnimal"),
    path('editarAnimal',views.editarAnimal,name="editarAnimal"),
    path('animales',views.animales,name="animales"),
    path('vacunas',views.vacunas,name="vacunas"),
]
