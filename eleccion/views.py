from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")



class Index(TemplateView):
    template_name = "eleccion/index.html"