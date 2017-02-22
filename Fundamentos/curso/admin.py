# encoding: utf-8
from django.contrib import admin
#from preguntasyrespuestas.models import Pregunta, Respuesta

# Register your models here.


from . import models
'''
class CursosInline(admin.StackedInline):
	model=models.Curso
	extra=3

class CursoAdmin(admin.ModelAdmin):
	inlines = [CursosInline]	
	list_display = ('nombre', 'pre_requisito','co_requisito','nivel','fecha_publicacion', 'publicado_hoy')
	list_filter= ['fecha_publicacion']
'''

admin.site.register(models.Curso)

