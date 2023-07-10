from datetime import date
from django.contrib.auth.models import User
from django.db import models


class Priority(models.Model):
    priority_choise = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    )
    value = models.CharField(max_length=20, choices=priority_choise)

    def __str__(self):
        return self.value

class Todo(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    parent_todo = models.ForeignKey('Todo', null=True, blank=True, on_delete=models.CASCADE, related_name='todos')
    completed = models.BooleanField(default=False)
    mod_date = models.DateField(default=date.today)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=False)
    label = models.ManyToManyField('Label', blank=True, null=True)

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

