import asyncio
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from database.models import Base

# Абсолютный путь к БД — работает независимо от того, откуда запущен бот
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # корень проекта
DB_PATH = os.path.join(BASE_DIR, "database", "DataBase.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(DATABASE_URL)#, echo=True)

session = sessionmaker(
    bind=engine,                 # Привязываем движок к сессии
    expire_on_commit=False      # Данные не сбрасываются после commit
)

def init_db():
    """Инициализация базы данных - создание таблиц"""
    Base.metadata.create_all(bind=engine)