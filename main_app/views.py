from django.shortcuts import render
from django.views import View #HANDLES REQUESTS
from django.http import HttpResponse #HANDLES RESPONSE
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView 
from django.urls import reverse
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
        title = self.request.GET.get("name")
        if title != None:
            context["tasks"] = Task.objects.filter(title__icontains=title, user=self.request.user)
            context["header"] = f"Searching for {title}"
        else:
            context["tasks"] = Task.objects.filter(user=self.request.user)
            context["header"] = "Tasks"
        return context

class TaskCreate(CreateView):
    model = Task 
    fields = '__all__'
    template_name = 'task_create.html'
    success_url = '/tasks/'

class TaskDetail(DetailView):
    model = Task 
    template_name = 'task_detail.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_update.html'
    success_url = '/tasks/'

class TaskDelete(DeleteView):
    model = Task 
    template_name = 'task_delete_confirmation.html'
    success_url = '/tasks/'

