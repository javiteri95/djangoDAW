# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Noticias(models.Model):
    
    titulo = models.CharField(max_length=100)
    Contenido = models.TextField()
    url_image = models.CharField(max_length=100)
    tag =  models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titulo

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'