from django.http import JsonResponse
from django.shortcuts import render
from .models import Todo


"""Если снова делать migrate. ТО!!! комитить эти строки"""
todos = Todo.objects.all()
todos_data = [todo for todo in todos.values('id', 'name', 'description', 'completed')]

def todo_json(request):
    return JsonResponse({'todos': todos_data})

"""Возможность сохранять новый todo сразу в базу. Но так как пока нету красивой привязки"""
"""к user'у в create-форме(через Имя например) то реализовано на костыле(через user_1)"""
def todo_save(todo_):
    Todo(
        id=todo_["id"],
        name=todo_["name"],
        description=todo_["description"],
        user_id=1
    ).save()

def home(request):
    if request.method == "GET":
        return render(request, 'todos.html', {'todos': todos_data})
    elif request.method == "POST":
        todo = dict(request.POST)
        for key in todo:
            todo[key] = todo[key][0]
        todo["id"] = len(todos_data)+1
        todos_data.append({"id": todo["id"], "name": todo["name"],
                           "description": todo["description"], "completed": False})
#       todo_save(todo)
        return render(request, "todos.html", {"todos": todos_data})

def get_todo(request, id):
    return render(request, 'todos.html', {'todos': [todos_data[id-1]]})

def create_todo(request):
    return render(request, "create_todo.html")