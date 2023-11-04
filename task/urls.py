from django.urls import path 
from .views import list_task, add_task,delete_task,update_task


app_name="task"
urlpatterns=[
    path("tasks",list_task, name="list_task"),
    path("add",add_task,name="add_task"),
    path("delete/<int:task_id>",delete_task,name="delete_task"),
    path("update/<int:task_id>",update_task,name="update_task")
]
