from django.http import JsonResponse
from django.shortcuts import render
from .models import Todo
from .models_func import todo_save, todos_data


def todo_json(request):
    return JsonResponse({'todos': todos_data()})

def home(request):
    if request.method == "GET":
        return render(request, 'todos.html', {'todos': todos_data()})
    elif request.method == "POST":
        todo = dict(request.POST)
        for key in todo:
            todo[key] = todo[key][0]
        todo["id"] = len(Todo.objects.all())+1
        todo["user_id"] = int(todo["user_id"])
        todo_save(todo)
        return render(request, "todos.html", {"todos": todos_data()})

def get_todo(request, id):
    return render(request, 'todos.html', {'todos': [todos_data()[id-1]]})

def create_todo(request):
    return render(request, "create_todo.html")