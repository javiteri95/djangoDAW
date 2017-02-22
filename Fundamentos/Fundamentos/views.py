
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.contrib.auth import authenticate, login, logout 


def home(request):
	return render(request, "home.html", {'home': home})

