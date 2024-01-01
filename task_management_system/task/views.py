from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def task(request):
    if request.method == "POST":
        task_forms = forms.TaskForm(request.POST)
        if task_forms.is_valid():
            task_forms.save()
            return redirect("home")
    else:
        task_forms = forms.TaskForm()
    return render(request, "task.html", {"form": task_forms})