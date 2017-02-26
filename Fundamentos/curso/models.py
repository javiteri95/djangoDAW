# Create your models here.

# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    pre_requisito = models.CharField(max_length=100)
    co_requisito = models.CharField(max_length=100)
    nivel = models.CharField(max_length=10)
    file_silabus = models.FileField(upload_to='media/', blank=True)
    file_politicas = models.FileField(upload_to='media/', blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'
