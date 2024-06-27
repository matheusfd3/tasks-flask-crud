from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data['description'])
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    output = {
        "tasks": [
            task.to_dict() for task in tasks
        ],
        "total_tasks": len(tasks)
    }
    return jsonify(output), 200

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({"message": "Task not found"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        data = request.get_json()
        task.title = data['title']
        task.description = data['description']
        task.completed = data['completed']
        return jsonify({"message": "Task updated successfully"}), 200
    return jsonify({"message": "Task not found"}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)