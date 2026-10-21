
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

app.config["DATABASE"] = os.environ.get(
    "TODO_DATABASE",
    os.path.join(os.path.dirname(__file__), "tasks.db")
)

REQUEST_COUNT = Counter(
    "todo_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)


@app.before_request
def count_requests():
    if request.endpoint != "metrics":
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.endpoint or "unknown"
        ).inc()


def get_db():
    connection = sqlite3.connect(app.config["DATABASE"])
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    connection.commit()
    connection.close()


@app.route("/")
def index():
    init_db()
    connection = get_db()
    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed
    connection.close()

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()

    if title:
        init_db()
        connection = get_db()
        connection.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )
        connection.commit()
        connection.close()

    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    init_db()
    connection = get_db()
    connection.execute(
        "UPDATE tasks SET completed = CASE completed "
        "WHEN 0 THEN 1 ELSE 0 END WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    init_db()
    connection = get_db()
    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


@app.route("/metrics")
def metrics():
    return (
        generate_latest(),
        200,
        {"Content-Type": CONTENT_TYPE_LATEST}
    )


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
