# encoding: utf-8
from django.contrib import admin
from equipo.models import Coordinador, Profesores

# Register your models here.


from . import models


admin.site.register(models.Coordinador)
admin.site.register(models.Profesores)
