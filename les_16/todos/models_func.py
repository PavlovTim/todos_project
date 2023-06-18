from .models import Todo

def todos_data():
    return [todo for todo in Todo.objects.all().values('id', 'name', 'description', 'completed')]

def todo_save(todo_):
    Todo(
        id=todo_["id"],
        name=todo_["name"],
        description=todo_["description"],
        user_id=todo_["user_id"]
    ).save()