from django.shortcuts import render, redirect
from task.models import TaskModel
from task.forms import TaskForm


def index(request):
    task = TaskModel.objects.all()
    return render(request, "index.html", {"data": task})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("home")
    return render(request, "task.html", {"form": task_form})


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect("home")