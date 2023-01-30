from django.shortcuts import render
from django.views import View #HANDLES REQUESTS
from django.http import HttpResponse #HANDLES RESPONSE


# Create your views here.

class Home(View):
    def get (self, request):
        return HttpResponse('Task Manager Home')


#ABOUT PAGE CLASS W/ FUNCTION 
class About(View):

    def get(self, request):
        return HttpResponse("Developer About Page")