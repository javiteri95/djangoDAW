# Create your models here.

# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Curso(models.Model):
    descripcion = models.CharField(max_length=500)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    nivel =  models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'


class Materias(models.Model):
    curso = models.ForeignKey(Curso)
    contenido = models.TextField()

    def __str__(self):
        return self.contenido
