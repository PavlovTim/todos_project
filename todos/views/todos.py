from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from les_16.settings import CACHE_TIME
from todos.models import Todo
from todos.forms import TodoForm, TodoUpdateForm, UserRegistrationForm, LoginForm
from todos.tasks import log_once_day


def todos(request):
    log_once_day()
    if request.method == "GET":
        return render(request, 'todos.html', {'todos': Todo.objects.all()})


@cache_page(CACHE_TIME)
def get_todo(request, todo_id):
    try:
        todo_object = Todo.objects.get(id=todo_id)
        dougth_todo = Todo.objects.filter(parent_todo=todo_object)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Todo not found.'})
    return render(request, 'todos.html', {'todos': [todo_object]+list(dougth_todo)})


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos")
        else:
            return render(request, "create_todo.html", {"form": form})
    return render(request, "create_todo.html", {"form": TodoForm()})


def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todos")
    return render(request, "update_todo.html", {"form": form})


@csrf_exempt
def delete_todo(request, todo_id):
    if request.method == "POST":
        Todo.objects.get(id=todo_id).delete()
        return redirect("todos")


@csrf_exempt
def complete_todo(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.completed = True
        todo.save()
        return JsonResponse({"status": 200, "message": "Post successfully updated"})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


