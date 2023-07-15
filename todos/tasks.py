from datetime import date, timedelta
from celery import shared_task
from django.contrib.auth.models import User
from les_16.celery import app
from todos.models import Todo


@app.task
def log_once_day():
    _dict = {}
    for user in User.objects.all():
        _dict[user.username] = []
        for todo in user.todos.all():
            if todo.mod_date == (date.today() - timedelta(days=1)):
                _dict[user.username].append(todo.name)
        if not _dict[user.username]:
            del (_dict[user.username])
        else:
            with open(f"logs/{user.id}+{date.today()}.txt", 'w') as out:
                for val in _dict[user.username]:
                    out.write(f"{val}\n")
