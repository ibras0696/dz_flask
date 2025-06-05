from pprint import pprint

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, delete
from sqlalchemy.orm import declarative_base

from database.db import session, init_db
from database.models import Movies


def add_movie(title: str, genre: str, year: int, rating: float, description: str):
    '''

    :param title: Название фильма
    :param genre: Жанр
    :param year: Год выпуска
    :param rating: Рейтинг
    :param description: Описание
    :return:
    '''
    with session() as conn:
        movie = Movies(
            title=title,
            genre=genre,
            year=year,
            rating=rating,
            description=description
        )
        try:
            conn.add(movie)
            conn.commit()
            return True
        except IntegrityError:
            conn.rollback()
            return False


def get_movies(title: str):
    with session() as conn:
        stmt = conn.query(Movies).filter(Movies.title.like(f'%{title}%')).all()
        return [
            {
                'id': movie.id,
                'title': movie.title,
                'genre': movie.genre,
                'year': movie.year,
                'rating': movie.rating,
                'description': movie.description

             } for movie in stmt
        ]


def delete_movie(title: str):
    '''
    Удаление фильма
    :param title: Название
    :return:
    '''
    with session() as conn:
       try:
          stmt = delete(Movies).where(Movies.title == title)
          conn.execute(stmt)
          conn.commit()
          return True
       except IntegrityError:
           conn.rollback()
           return False


# init_db()
# # print(delete_movie('Тест'))
