from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso!"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks_dict = [task.to_dict() for task in tasks]
    output = {
        "tasks": tasks_dict,
        "total_tasks": len(tasks)
    }
    return jsonify(output)

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task.id == task_id:
            return jsonify(task.to_dict())
    return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)