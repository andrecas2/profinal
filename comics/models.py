from django.db import models
from django.contrib import admin


class Editorial(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")


    class Meta:
                verbose_name="Editorial"
                verbose_name_plural="Editoriales"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Autor(models.Model):

    nombre  =   models.CharField(max_length=60)


    class Meta:
                verbose_name="Autor"
                verbose_name_plural="Autores"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Comic(models.Model):

    nombre = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,related_name="keyeditorial")
    autor = models.ManyToManyField(Autor,verbose_name="Autor",related_name="keyautor")

    class Meta:
                verbose_name="Comic"
                verbose_name_plural="Comics"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre
