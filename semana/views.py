# encoding: utf-8
from django.http import HttpResponse
from semana.models import Semana, Recurso
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def semana(request):
    semanas = Semana.objects.all()
    recursos = Recurso.objects.all()
    context = {
        'semanas': semanas,
        'recursos': recursos
    }
    return render(request, 'semana.html', context)
