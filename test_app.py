from flask import Flask
from api import app, TODOS
import random
import pytest

app.config['TESTING'] = True
test_c = app.test_client()


def test_todolist_get():
    response = test_c.get('/todos')
    assert response.status_code == 200


def test_each_todo_get():
    if TODOS.keys():
        for todo in TODOS.keys():
            todo_item = test_c.get('/todos/{}'.format(todo))
            assert todo_item.status_code == 200


def test_random_todo_delete():
    todo_id = random.choice(list(TODOS.keys()))
    del_response = test_c.delete('/todos/{}'.format(todo_id))
    assert del_response.status_code == 204


def test_each_todo_put():
    if TODOS.keys():
        for todo_id in TODOS.keys():
            completed_false = TODOS[todo_id]['Completed']
            completed_true = TODOS[todo_id]['Completed'] = 'true'
            assert completed_false == 'false'
            assert completed_true == 'true'


def test_todolist_post():
    previous_todo_count = len(TODOS.keys())
    todo_id = 'todo' + str(int(max(TODOS.keys()).lstrip('todo')) + 1)
    TODOS[todo_id] = {'task': 'TEST'}
    updated_todo_count = len(TODOS.keys())
    assert previous_todo_count + 1 == updated_todo_count
