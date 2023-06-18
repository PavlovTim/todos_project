from django.forms import model_to_dict
from django.http import JsonResponse
from todos.models_func import todos_data
from todos.models import Todo


def todos_json(request):
    return JsonResponse({'todos': todos_data()})

def get_todo_json(request, todo_id: int):
    try:
        todo_object = Todo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Todo not found.'})
    return JsonResponse({'todo': model_to_dict(todo_object)})