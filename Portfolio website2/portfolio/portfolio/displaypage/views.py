from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.template import loader
# Create your views here.

def index(request):
	template = loader.get_template('displaypage/index.html')
	return HttpResponse(template.render(request))