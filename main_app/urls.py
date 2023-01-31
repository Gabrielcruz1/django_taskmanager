from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    #ROUTE IS TASKS PLURAL 
    path('tasks/', views.TaskList.as_view(), name="task_list" ),
    path('tasks/new/', views.TaskCreate.as_view(), name="task_create"),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name="task_detail"),

]