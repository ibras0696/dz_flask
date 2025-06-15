from pprint import pprint

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, delete
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.sync import update

from database.db import session
from to_do_flask.database.models import Task


def get_tasks():
    with session() as conn:
        tasks = conn.query(Task).all()
        return tasks


def add_tasks(title: str, description: str):
    with session() as conn:
        task = Task(title=title, description=description, status='В Процессе')
        try:
            conn.add(task)
            conn.commit()  # ← добавь эту строку!
        except IntegrityError:
            return False
        except Exception as ex:
            print(f'Ошибка: {ex}')


def delete_task(task_id: int):
    with session() as conn:
        try:
            stmt = delete(Task).where(Task.id == task_id)
            conn.execute(stmt)
            conn.commit()
            return True
        except IntegrityError:
            return False
        except Exception as ex:
            print(f'Ошибка: {ex}')


def update_task_status(task_id: int, status: str):
    with session() as conn:
        try:
            task = conn.get(Task, task_id)
            if task:
                task.status = status
                conn.commit()
        except IntegrityError:
            return False
        except Exception as ex:
            print(f'Ошибка: {ex}')