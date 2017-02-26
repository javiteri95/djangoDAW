# encoding: utf-8
from django.contrib import admin
from ayudantias.models import Aulas, Ayudantes, Ayudantias

# Register your models here.


from . import models


admin.site.register(models.Ayudantes)
admin.site.register(models.Aulas)
admin.site.register(models.Ayudantias)
