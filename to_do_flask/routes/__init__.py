from flask import Flask

from .task_routes import tasks_bp


def init_routs(app: Flask):
    app.register_blueprint(tasks_bp, url_prefix='/tasks')