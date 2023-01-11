from enum import unique
from cv2 import repeat
from django.db import models
from tabnanny import verbose

        
class Vacas(models.Model):
    id_vaca=models.AutoField(primary_key=True, verbose_name="id_vaca")
    nombre_empleado=models.CharField(max_length=150, verbose_name='Nombre_empleado')
    nombre_vaca= models.CharField(max_length=100,unique=True, verbose_name='Nombre_vaca')
    num_vaca= models.IntegerField(verbose_name='Numero_vaca')
    color_vaca= models.CharField(max_length=50, verbose_name='Color_vaca')
    fecha_nacimiento=models.DateField(null=False, verbose_name='Fecha_nacimiento')
    raza_vaca= models.CharField(max_length=100, verbose_name='Raza_vaca')
    Peso_vaca= models.CharField(max_length=100, verbose_name='Peso_vaca')
    
    def __str__(self):
        fila= "Nombre: "+self.nombre_vaca+" - "+"Número: "+self.num_vaca
        return fila
   
    class Meta:
        verbose_name = 'Vaca'
        verbose_name_plural = 'Vaca'
        db_table= 'Vaca'

class Produccion(models.Model):
    id_produccion=models.AutoField(primary_key=True, verbose_name="id_produccion")
    fecha_produc= models.DateField(verbose_name='Fecha_produc')
    horario= models.CharField(max_length=100,verbose_name='Horario')
    comida= models.CharField(max_length=100, verbose_name='Comida')
    leche= models.CharField(max_length=100, verbose_name='Leche')
    id_vaca= models.ForeignKey(Vacas, null=False, blank=True, on_delete=models.CASCADE)
     
    def __str__(self):
        fila= "Fecha: "+self.fecha_produc+" - "+"Horario: "+self.horario
        return fila
    
    class Meta:
        verbose_name = 'Produccion'
        verbose_name_plural = 'Produccions'
        db_table= 'Produccion'
