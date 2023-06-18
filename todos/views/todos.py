from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt

from todos.models import Todo
from todos.models_func import todo_save, todos_data
from todos.forms import TodoForm


def todos(request):
    if request.method == "GET":
        return render(request, 'todos.html', {'todos': Todo.objects.all()})


def get_todo(request, todo_id):
    try:
        todo_object = Todo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Todo not found.'})
    return render(request, 'todos.html', {'todos': [todo_object]})


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos")
        else:
            return render(request, "create_todo.html", {"form": form})
    return render(request, "create_todo.html", {"form": TodoForm()})


@csrf_exempt
def delete_todo(request, todo_id):
    if request.method == "POST":
        Todo.objects.get(id=todo_id).delete()
        return redirect("todos")
