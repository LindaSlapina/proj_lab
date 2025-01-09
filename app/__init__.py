from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import os

# Инициализация Flask-приложения
app = Flask(__name__)

# Конфигурация базы данных
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "datubaze.db")}'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datubaze.db?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация SQLAlchemy
db = SQLAlchemy(app)

from app import routes, model

with app.app_context():
    from app.model import Darbinieki
    db.create_all()
    inspector = inspect(db.engine)
    if 'darbinieki' in inspector.get_table_names():
        # Проверяем, есть ли записи в таблице 'darbinieki'
        if not db.session.query(Darbinieki).first():
            # Если записей нет, добавляем администратора
            admin1 = Darbinieki(login='Admin1', password='12345')
            admin2 = Darbinieki(login='Admin2', password='67890')
            db.session.add(admin1)
            db.session.add(admin2)
            db.session.commit()
    else:
        # Логируем ошибку, если таблица почему-то не создалась
        print("Таблица 'darbinieki' не создана.") 


