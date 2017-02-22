# Create your models here.

# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Equipo(models.Model):
    
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    foto = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    mail =  models.CharField(max_length=100)
    titulo = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'

