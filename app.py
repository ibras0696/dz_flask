from flask import Flask, request, jsonify
from database.crud import get_movies, add_movie, delete_movie


app = Flask(__name__)


@app.route('/')
def start_cmd():
    return 'Основной сайт фласк апи Фильмов'


@app.route('/movies/<movie>')
def movies_cmd(movie):
    data = get_movies(movie)
    return jsonify(data)


@app.route('/movies/add/', methods=['POST'])
def post_movie_cmd():
    title = request.headers.get('title')
    genre = request.headers.get('genre')
    year = request.headers.get('year')
    rating = request.headers.get('rating')
    description = request.headers.get('description')
    if title:
        try:
            result = add_movie(
            title=title,
            genre=genre,
            year=int(year),
            rating=float(rating),
            description=description
        )
        except Exception as ex:
            return f'Ошибка: {ex}'
        else:
            if result:
                return 'Фильм Успешно добавлен'
            else:
                return f'Такой фильм уже есть: {title}'


@app.route('/movies/delete/<title>')
def delete_movies_cmd(title):
    print(title)
    result = delete_movie(title=title)
    if result:
        return f'Фильм: {title} удален'
    else:
        return f'Нет такого фильма'


if __name__ == '__main__':
    app.run()