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


class Task:
    def __init__(self, title):
        self.title = title 


class TaskList(TemplateView):
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task
        return context


