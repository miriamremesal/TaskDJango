from django.shortcuts import render
from .models import Task 

def task_list(request):
    task = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'task': task})