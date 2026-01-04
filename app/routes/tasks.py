from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Task

task_bp = Blueprint("tasks", __name__)


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "is_completed": task.is_completed,
        "created_at": task.created_at.isoformat(),
        "updated_at": task.updated_at.isoformat(),
    }


@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    title = data.get("title", "").strip()
    description = data.get("description")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    if len(title) > 120:
        return jsonify({"error": "Title must be ≤ 120 characters"}), 400

    task = Task(
        title=title,
        description=description
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task_to_dict(task)), 201


@task_bp.route("/", methods=["GET"])
def get_tasks():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    completed = request.args.get("completed")
    sort = request.args.get("sort", "created_at")
    order = request.args.get("order", "desc")

    query = Task.query

    # 🔹 Filtering
    if completed is not None:
        if completed.lower() == "true":
            query = query.filter(Task.is_completed.is_(True))
        elif completed.lower() == "false":
            query = query.filter(Task.is_completed.is_(False))
        else:
            return jsonify({"error": "completed must be true or false"}), 400

    # 🔹 Sorting
    if hasattr(Task, sort):
        column = getattr(Task, sort)
        if order == "asc":
            query = query.order_by(column.asc())
        else:
            query = query.order_by(column.desc())
    else:
        return jsonify({"error": "Invalid sort field"}), 400

    # 🔹 Pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages,
        "tasks": [task_to_dict(task) for task in pagination.items]
    })


# get all single task
@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task_to_dict(task))


#update taskS
@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    if "title" in data:
        title = data["title"].strip()
        if not title:
            return jsonify({"error": "Title cannot be empty"}), 400
        task.title = title

    if "description" in data:
        task.description = data["description"]

    if "is_completed" in data:
        if not isinstance(data["is_completed"], bool):
            return jsonify({"error": "is_completed must be boolean"}), 400
        task.is_completed = data["is_completed"]

    db.session.commit()

    return jsonify(task_to_dict(task))

# delete task
@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"})
