from django.shortcuts import render,redirect
from .models import Task
from .form import TaskForm
# Create your views here.
def list_task(request):
    tasks=Task.objects.all()
    print(tasks)
    context= {'tasks':tasks}
    return render(request,"task_list.html",context)

def add_task(request):
    form= TaskForm()
    if request.method=="POST":
        data= TaskForm(request.POST)
        if data.is_valid(): 
            data.save()
            return redirect("/tasks")
    context={'form':form}
    return render(request,"add_task.html",context)

def delete_task(request,task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("/tasks")

def update_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.completed= True
    task.save()
    return render(request,"task_list.html")

