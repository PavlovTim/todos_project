from django.urls import path
from todos.views import todos

urlpatterns = [
    path('', todos.todos, name='todos'),
    path('<int:todo_id>', todos.get_todo, name='get_todo'),
    path('create', todos.create_todo, name='create_todo'),
    path('delete/<int:todo_id>', todos.delete_todo, name='delete_todo'),
    path('update/<int:todo_id>/', todos.update_todo, name='update_todo'),
    path('complete/<int:todo_id>/>', todos.complete_todo, name='complete_todo'),
    path('login', todos.user_login, name='user_login'),
    path('register', todos.user_register, name='user_register'),
]