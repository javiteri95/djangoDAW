from django.shortcuts import render

# encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def ranking(request):
    return render(request, 'ranking.html')
