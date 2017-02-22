# encoding: utf-8
from django.contrib import admin
#from preguntasyrespuestas.models import Pregunta, Respuesta

# Register your models here.


from . import models
'''
class RespuestaInline(admin.StackedInline):
	model=models.Materias
	extra=3
'''
'''
class PreguntaAdmin(admin.ModelAdmin):
	inlines = [RespuestaInline]	
	list_display = ('descripcion', 'fecha_publicacion', 'publicado_hoy')
	list_filter= ['fecha_publicacion']
'''
	
admin.site.register(models.Curso)
admin.site.register(models.Materias)

