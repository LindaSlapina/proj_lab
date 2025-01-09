from flask import Flask, render_template, redirect, url_for, request, flash

from app import app, db
from app.model import Pasutijums, Darbinieki
import os
import logging
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/kontaktinfo')
def kontaktinfo():
    return render_template('kontaktinfo.html')

@app.route('/ielogosanas')
def ielogosanas():
    return render_template('ielogosanas.html')

@app.route('/adminmain')
def adminmain():
    orders = Pasutijums.query.all()
    return render_template('adminmain.html', orders=orders)


@app.route('/pasutisana')
def pasutisana():
    return render_template('pasutisana.html')

@app.route('/ielogosanas', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        # Поиск пользователя по логину
        user = Darbinieki.query.filter_by(login=login).first()

        if user and user.password == password:  # Проверка пароля
            # Авторизация успешна
            return redirect(url_for('adminmain'))  # Перенаправление на главную
        else:
            error_message = 'Nepareizs logins vai parole!'

    return render_template('ielogosanas.html', error_message=error_message)

@app.route('/update_status', methods=['POST'])
def update_status():
    try:
        # Получаем данные из запроса
        order_id = request.form['id']
        new_status = request.form['status']

        # Ищем заказ по ID
        order = Pasutijums.query.get(order_id)

        if order:
            # Обновляем статус
            order.materiala_statuss = new_status

            # Сохраняем изменения
            db.session.commit()

            # Успешный ответ
            return "Status updated successfully", 200
        else:
            # Если заказ не найден
            return "Order not found", 404

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error updating status: {e}")
        return f"Error: {e}", 400

    finally:
        db.session.close()
 
@app.route('/submit', methods=['POST'])   
def submit():
    try:
        vards = request.form['vards']
        uzvards = request.form['uzvards']
        numurs = request.form['numurs']
        epasts = request.form['epasts']
        piegades_adrese = f"{request.form['pilseta']}, {request.form['iela']}, {request.form['majasNR']}"
        izmers = request.form['izmers']
        daudzums = request.form['gab']
        komentari = request.form['komentari']
        faila_aug = request.files['faila_aug']
        materiala_statuss='Nav zināms'

        # Сохранение файла
        filename = None
        if faila_aug:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], faila_aug.filename)
            faila_aug.save(filename)

        # Создание записи
        new_order = Pasutijums(
            vards=vards,
            uzvards=uzvards,
            TelefonaNumurs=numurs,
            epasts=epasts,
            PiegadesAdrese=piegades_adrese,
            izmers=izmers,
            daudzums=int(daudzums),
            komentari=komentari,
            FailaAugšupielāde=filename,  # Убедитесь, что используете правильное имя колонки
            materiala_statuss=materiala_statuss
        )

        db.session.add(new_order)
        db.session.commit()

        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error: {e}")
        return f"Error: {e}", 400

    finally:
        db.session.close()