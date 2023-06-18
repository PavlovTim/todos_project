from django.urls import path
from todos.views import todos

urlpatterns = [
    path('', todos.todos, name='todos'),
    path('<int:todo_id>', todos.get_todo, name='get_todo'),
    path('create', todos.create_todo, name='create_todo'),
    path('delete/<int:todo_id>', todos.delete_todo, name='delete_todo'),
]