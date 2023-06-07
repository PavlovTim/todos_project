from django.http import JsonResponse
from django.shortcuts import render
import requests
from django.conf import settings


class Todos:
    def __init__(self, todo=None):
        self.todo = todo or []

    def __iter__(self):
        self.i = -1
        self.count = len(self.todo)
        return self

    def __next__(self):
        if self.i < self.count:
            self.i += 1
            return self.todo[self.i]
        raise StopIteration

    def __getitem__(self, item):
        return self.todo[item]

    def append_todo(self, todo_):
        self.todo.append(todo_)

    def get_by_id(self, id):
        return next((i for i in self.todo if i.id == id), None)

    def output_in_json(self):
        json_list = []
        for i in self.todo:
            json_list.append(i.for_json_out())
        return json_list

class Todo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    def for_json_out(self):
        return {
            "userId": self.userId,
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }


todos = Todos()
for i in requests.get(settings.URL).json():
    todos.append_todo(Todo(i['userId'], i['id'], i['title'], i['completed']))

def todo_db(request):
    from .models import Todo
    todos = Todo.objects.all()
    todos_data = [todo for todo in todos.values('name','description', 'completed')]
    return JsonResponse({'todos': todos_data})

def json_out(request):
    return JsonResponse({'todos': todos.output_in_json()})

def home(request):
    if request.method == "GET":
        return render(request, 'todos.html', {'todos': todos.output_in_json()})
    elif request.method == "POST":
        todo = dict(request.POST)
        for key in todo:
            todo[key] = todo[key][0]
        todo["id"] = int(todo["id"])
        todo["userId"] = int(todo["userId"])
        todos.append_todo(Todo(todo['userId'], todo['id'],
                               todo['title'], todo['completed']))
        return render(request, "todos.html", {"todos": todos})

def get_todo(request, id):
    return render(request, 'todos.html', {'todos': [todos.get_by_id(id).for_json_out()]})

def create_todo(request):
    return render(request, "create_todo.html")