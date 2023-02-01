from django.shortcuts import render, redirect
from django.views import View #HANDLES REQUESTS
from django.http import HttpResponse #HANDLES RESPONSE
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView 
from django.urls import reverse 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task 
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

#ABOUT PAGE CLASS W/ FUNCTION 
class About(TemplateView):
    template_name = "about.html"




class Signup(View):
    #FORM TO BE FILLED OUT 
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    #VALIDATE FORM AND LOGIN USER ON SUBMIT
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
        else: 
            context = {"form": form}
            return render(request, "registraion/signup.html", context)


@method_decorator(login_required, name='dispatch')
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
    fields = ['title', 'description', 'complete']
    template_name = 'task_create.html'
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(TaskCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('task_detail', kwargs={'pk': self.object.pk})

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

