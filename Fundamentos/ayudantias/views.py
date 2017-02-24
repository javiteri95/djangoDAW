# encoding: utf-8
from django.http import HttpResponse
from curso.models import Curso
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def ayudantia(request):
    ayudantias = Ayudantia.objects.all()
    return render(request, 'ayudantias.html', {'ayudantias': ayudantias})

