# Create your models here.

# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.


class Ayudantes(models.Model):
    numeric = RegexValidator(r'^[0-9]*$',  message='solo valido numeros.')
    matricula = models.CharField(
        max_length=9, primary_key=True, validators=[numeric])
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.matricula + ' - ' + self.nombre

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'


class Aulas(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    latitud = models.FloatField(blank=False)
    longitud = models.FloatField(blank=False)

    def __str__(self):
        return self.codigo

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'


class Ayudantias(models.Model):
    DAYS_CHOICES = (
        ("Lunes", "Lunes"),
        ("Martes", "Martes"),
        ("Miercoles", "Miercoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
    )
    ayudante = models.ForeignKey(Ayudantes, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aulas, on_delete=models.CASCADE)
    dia = models.CharField(max_length=9, choices=DAYS_CHOICES, blank=False)
    horaInicio = models.TimeField(verbose_name='Empieza')
    horaFin = models.TimeField(verbose_name='Finaliza')

    def __str__(self):
        return self.ayudante.nombre + ' - ' + self.aula.codigo + ' - ' + self.dia

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = '¿Preguntando hoy?'
