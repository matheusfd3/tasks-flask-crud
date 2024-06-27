import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000/'
tasks = []

def test_create_task():
    new_task = {
        "title": "New Task",
        "description": "Description of task"
    }
    response = requests.post(BASE_URL + 'tasks', json=new_task)
    assert response.status_code == 201
    response_body = response.json()
    assert "message" in response_body
    assert "id" in response_body
    tasks.append(response_body["id"])

def test_get_tasks():
    response = requests.get(BASE_URL + 'tasks')
    assert response.status_code == 200
    response_body = response.json()
    assert "tasks" in response_body
    assert "total_tasks" in response_body

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(BASE_URL + 'tasks/' + str(task_id))
        assert response.status_code == 200
        response_body = response.json()
        assert task_id == response_body["id"]

def test_update_task():
    if tasks:
        task_id = tasks[0]
        updated_task = {
            "title": "Updated Task",
            "description": "Updated description of task",
            "completed": True
        }
        response = requests.put(BASE_URL + 'tasks/' + str(task_id), json=updated_task)
        assert response.status_code == 200
        response_body = response.json()
        assert "message" in response_body

        response = requests.get(BASE_URL + 'tasks/' + str(task_id))
        assert response.status_code == 200
        response_body = response.json()
        assert updated_task["title"] == response_body["title"]
        assert updated_task["description"] == response_body["description"]
        assert updated_task["completed"] == response_body["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(BASE_URL + 'tasks/' + str(task_id))
        assert response.status_code == 200

        response = requests.get(BASE_URL + 'tasks/' + str(task_id))
        assert response.status_code == 404