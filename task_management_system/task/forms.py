from django import forms
from .models import TaskModel


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = "__all__"
        widgets = {"assigned_date": forms.TextInput(attrs={"type": "date"})}
        labels = {
            "taskTitle": "Task Name",
            "taskDescription": "Description",
            "is_completed": "Completed",
            "category": "Categories",
        }