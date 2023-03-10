from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    #ROUTE IS TASKS PLURAL 
    path('tasks/', views.TaskList.as_view(), name="task_list" ),
    path('tasks/new/', views.TaskCreate.as_view(), name="task_create"),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name="task_detail"),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name="task_update"),
    path('tasks/<int:pk>/delete', views.TaskDelete.as_view(), name="task_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")

]