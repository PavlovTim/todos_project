import pytest
from todos.tests.todos.test_app import test_data


@pytest.mark.django_db
def test_get_todos(client, test_data):
    response = client.get("/api/todos/")
    assert response.status_code == 200
    result = response.json()
    assert len(result["todos"]) == 3
    assert result["todos"][0]["mod_date"] == '2023-07-17'


@pytest.mark.django_db
def test_get_todo(client, test_data):
    response = client.get("/api/todos/1")
    assert response.status_code == 200
    assert response.json()['todo'] == {
        "name": "click",
        'description': "click-clack",
        'user': 1,
        'priority': 1,
        'completed': False,
        'id': 1,
        'label': ['Homework', 'Outside'],
        'mod_date': '2023-07-17',
        'parent_todo': None
    }

