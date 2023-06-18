from django.urls import path
from todos.views.api import todos_json, get_todo_json


urlpatterns = [
    path('', todos_json, name="todos_json"),
    path('<int:todo_id>', get_todo_json, name='todo_id_json')
]