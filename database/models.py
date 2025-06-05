from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)

    title = Column(String(50), unique=True)
    genre = Column(String(50))
    year = Column(Integer)
    rating = Column(Float)
    description = Column(String(200))
