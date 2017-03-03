# encoding: utf-8
from django.http import HttpResponse
from equipo.models import Profesores, Coordinador
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def equipo(request):

    profesores = Profesores.objects.all()
    coordina = Coordinador.objects.all()
    for coord in coordina:
        cod_id = coord.id
    coordinador = Coordinador.objects.get(id=cod_id)

    context = {
        'coordinador': coordinador,
        'profesores': profesores
    }
    return render(request, 'equipo.html', context)
