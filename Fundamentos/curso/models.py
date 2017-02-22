# Create your models here.

# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    pre_requisito = models.TextField(max_length=100)
    co_requisito = models.TextField(max_length=100)
    nivel =  models.CharField(max_length=10)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'

