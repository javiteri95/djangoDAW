# encoding: utf-8
from  django import forms
from noticias.models import Noticias

class NoticiasForm(forms.ModelForm):
	class Meta:
		model = Noticias
		fields = "__all__"


