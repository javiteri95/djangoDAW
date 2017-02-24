
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
# encoding: utf-8
class Semana(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'

class TipoRecurso(models.Model):
    TYPE_CHOICE = (
        ('V', 'video'),
        ('P', 'pdf'),
    )
    nombre = models.CharField(max_length=20)
    icono = models.CharField(max_length=300)
    tipo = models.CharField(max_length = 1, choices = TYPE_CHOICE)

    def __str__(self):
    	return self.nombre
		
class Recurso(models.Model):
	tipo = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
	semana = models.ForeignKey(Semana, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	file  = models.FileField(blank=True)
	url = models.URLField(blank=True)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.id) + ' - ' + self.nombre +  ' - ' + str(self.tipo)