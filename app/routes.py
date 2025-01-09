from flask import Flask, render_template, redirect, url_for, request

from app import app, db
from app.model import Pasutijums
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

@app.route('/pasutisana')
def pasutisana():
    return render_template('pasutisana.html')
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
            FailaAugšupielāde=filename  # Убедитесь, что используете правильное имя колонки
        )

        db.session.add(new_order)
        db.session.commit()

        return redirect(url_for('home'))

    except Exception as e:
        logging.error(f"Error: {e}")
        return f"Error: {e}", 400