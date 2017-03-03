# encoding: utf-8
from django.contrib import admin
#from preguntasyrespuestas.models import Pregunta, Respuesta

# Register your models here.


from . import models


admin.site.register(models.Noticias)

