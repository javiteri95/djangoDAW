"""Fundamentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Fundamentos.views import home
from curso.views import curso
from equipo.views import equipo
from ayudantias.views import ayudantia
from noticias import views
#from ranking.views import ranking

admin.autodiscover()

urlpatterns = [
    url(r'^admin/docs', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^cursos/$', curso, name='curso'),
    url(r'^equipos/$', equipo, name='equipo'),
    #url(r'^equipos/$', equipo, name='equipo'),
    url(r'^ayudantias/$', ayudantia, name='ayudantias'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^noticias/crear/$', views.crearNoticia, name='crearNoticia'),
]
