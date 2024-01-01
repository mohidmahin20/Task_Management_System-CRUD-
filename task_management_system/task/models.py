from django.db import models
from category.models import CategoryModel


# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    assigned_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.taskTitle