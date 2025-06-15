from uuid import uuid4

from flask import Flask, request

from database.db import init_db
from routes import init_routs

app = Flask(__name__)

# Устанавливаем секретный ключ
app.secret_key = f'{uuid4()}'  # Замените на уникальную и секретную строку

@app.route('/')
def start_hello_cmd():
    return f'Привет Hello World'



if __name__ == '__main__':
    init_db()
    init_routs(app)
    app.run(debug=True)