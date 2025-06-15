from flask import Blueprint, render_template, redirect, flash, request, url_for

from to_do_flask.database.crud import get_tasks, delete_task, add_tasks, update_task_status
from to_do_flask.database.models import Task

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/')
def get_all_tasks_cmd():
    tasks = get_tasks()
    return render_template('tasks.html', my_tasks=tasks)
    # return render_template('task_detail.html', my_tasks=tasks)

@tasks_bp.route('/<int:task_id>', methods=['POST'])
def delete_task_cmd(task_id):
    delete_task(task_id)
    return redirect(url_for('tasks.get_all_tasks_cmd'))


@tasks_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        add_tasks(title, description)
        flash('Задача добавлена успешно!')
        return redirect(url_for('tasks.get_all_tasks_cmd'))  # Исправлено здесь

    return render_template('add_task.html')


@tasks_bp.route('/<int:task_id>/update_status', methods=['POST'])
def update_task_status_cmd(task_id):
    new_status = request.form.get('status')
    update_task_status(task_id, new_status)
    flash('Статус задачи обновлен!')
    return redirect(url_for('tasks.get_all_tasks_cmd'))