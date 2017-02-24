# encoding: utf-8
from django.contrib import admin
from semana.models import Semana, Recurso, TipoRecurso

# Register your models here.


from . import models


class SemanaInline(admin.StackedInline):
    model = models.Recurso
    extra = 3


class SemanaAdmin(admin.ModelAdmin):
    inlines = [SemanaInline]
    list_display = ('titulo', 'fecha_publicacion', 'publicado_hoy')
    list_filter = ['fecha_publicacion']

admin.site.register(models.Semana, SemanaAdmin)
admin.site.register(models.TipoRecurso)