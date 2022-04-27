from django.http import HttpResponse
from django.shortcuts import render
from ast import Return
from .models import vacuna, animal



def inicio(request):
  return HttpResponse("<H1>HOLA MUNDO desde el itp</H1>")

  
def index(request):
    return render(request,'pagina/index.html')


def mostrarnombre(request,nom,edad):
    return HttpResponse("<h1>Hola tu nombre es %s y tu edad es de %s </h1>" %(nom,edad))

def informacion(request):
 return render(request,'pagina/info.html')

def informacion2(request):
     return render(request,'pagina/info2.html')
 
def crearAnimal(request):
     return render(request,'animales/crearAnimal.html')

def editarAnimal(request):
     return render(request,'animales/editarAnimal.html')

def animales(request):
     animales=animal.objects.raw('SELECT libreria_animal.id,libreria_animal.nombre,libreria_animal.edad,libreria_animal.genero,libreria_animal.telefono,libreria_vacuna.vacuna FROM animales.libreria_animal INNER JOIN animales.libreria_vacuna ON libreria_animal.vacuna_animal_id=libreria_vacuna.id')
     return render(request,'animales/indexAnimales.html',{'animales': animales})

def vacunas(request):
     vacunas=vacuna.objects.all()
     return render(request,'vacunas/vacunas.html',{'vacunas': vacunas})

def enviar(request):
    if(request.POST):
        recibedatos = request.POST.dict()
        nombre = recibedatos.get("nombre")  
        edad = recibedatos.get("edad")   
    return HttpResponse(" Hola tu  nombre es %s y tu edad es %s <BR> <a  class='btn btn-primary' href='informacioncontacto' role='button'>Regresar</a>" %(nombre,edad))


