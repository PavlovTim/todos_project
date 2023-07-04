import copy

from django.forms import model_to_dict
from django.http import JsonResponse
from todos.models import Todo


def todos_json(request):
    model_list = []
    for todo_object in Todo.objects.all():
        pr = todo_object.label.all()
        dict_ = model_to_dict(todo_object, exclude='label')
        dict_['label'] = [j.name for j in list(pr)]
        model_list.append(dict_)
    return JsonResponse({'todos': model_list})

def get_todo_json(request, todo_id: int):
    try:
        todo_object = Todo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Todo not found.'})
    pr = todo_object.label.all()
    dict_ = model_to_dict(todo_object, exclude='label')
    dict_['label'] = [j.name for j in list(pr)]
    return JsonResponse({'todo': dict_})