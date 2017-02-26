# encoding: utf-8
from django.http import HttpResponse
from ayudantias.models import Ayudantias
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def ayudantia(request):
    ayudantias = Ayudantias.objects.all()
    context = {
        'ayudantias': ayudantias,
        'aulas': aulas,
        'ayudantes': ayudantes
    }
    return render(request, 'ayudantias.html', context)
