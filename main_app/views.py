from django.shortcuts import render
from django.views import View #HANDLES REQUESTS
from django.http import HttpResponse #HANDLES RESPONSE
from django.views.generic.base import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"



#ABOUT PAGE CLASS W/ FUNCTION 
class About(TemplateView):
    template_name = "about.html"