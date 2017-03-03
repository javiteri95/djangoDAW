# encoding: utf-8
from django.http import HttpResponse
from curso.models import Curso
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def curso(request):
    # hago este for porque cuando se borra un registro y se guarda el id se
    # aumenta
    todos = Curso.objects.all()
    for curso in todos:
        cod_id = curso.id
    cursos = Curso.objects.get(id=cod_id)
    return render(request, 'curso.html', {'cursos': cursos})
