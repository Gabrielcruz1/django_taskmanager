from django.shortcuts import render
from django.views import View #HANDLES REQUESTS
from django.http import HttpResponse #HANDLES RESPONSE
from django.views.generic.base import TemplateView 
from .models import Task 

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

#ABOUT PAGE CLASS W/ FUNCTION 
class About(TemplateView):
    template_name = "about.html"




class TaskList(TemplateView):
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["tasks"] = Task.objects.filter(title__icontains=title)
        else:
            context["tasks"] = Task.objects.all()
        return context


