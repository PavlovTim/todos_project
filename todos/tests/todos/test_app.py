import pytest
from django.contrib.auth.models import User
from django.test import Client
from todos.models import Priority, Label, Todo


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def test_data():
    user_1 = User.objects.create_user(
        username='Tim',
        email='timtim@gmail.com',
        password='12345',
        is_active=True
    )
    user_2 = User.objects.create_user(
        username='Lera',
        email='valeron@gmail.com',
        password='12345',
        is_active=True
    )

    priority_1 = Priority(
        value="Low"
    )
    priority_1.save()
    priority_2 = Priority(
        value="Medium"
    )
    priority_2.save()
    priority_3 = Priority(
        value="High"
    )
    priority_3.save()

    label_1 = Label(
        name="Homework"
    )
    label_1.save()
    label_2 = Label(
        name="Outside"
    )
    label_2.save()

    todo_1 = Todo(
        name="click",
        description="click-clack",
        user=user_1,
        priority=priority_1,

    )
    todo_1.save()
    todo_1.label.add(label_1, label_2)
    todo_2 = Todo(
        name="management",
        description="fix management problems",
        user=user_1,
        completed=True,
        priority=priority_2,

    )
    todo_2.save()
    todo_3 = Todo(
        name="celebrate",
        description="celebrating a new coming",
        user=user_2,
        priority=priority_3,
    )
    todo_3.save()
    