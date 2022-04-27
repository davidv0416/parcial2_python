from django.db import models


class vacuna(models.Model):
    id=models.AutoField(primary_key=True)
    vacuna=models.CharField(max_length=100,verbose_name='vacuna',null=True)
    fecha=models.DateField(max_length=100,verbose_name='Direccion',null=True)

class animal(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Nombre',null=True)
    edad=models.CharField(max_length=100,verbose_name='Direccion',null=True)
    genero=models.CharField(max_length=100,verbose_name='Telefono',null=True)
    telefono=models.CharField(max_length=100,verbose_name='Correo',null=True)
    vacuna_animal = models.ForeignKey(vacuna, on_delete=models.CASCADE)




    
