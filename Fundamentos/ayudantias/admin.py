# encoding: utf-8
from django.contrib import admin
from ayudantias.models import Ayudantes, Aulas, Ayudantias

# Register your models here.


from . import models


class AyudantiasInline(admin.StackedInline):
    model = models.Ayudantias
    extra = 3


class AyudantesAdmin(admin.ModelAdmin):
    inlines = [AyudantiasInline]
    list_display = ('matricula', 'nombre', 'publicado_hoy')
    list_filter = ['fecha_publicacion']

admin.site.register(models.Ayudantes, AyudantesAdmin)
admin.site.register(models.Aulas)
