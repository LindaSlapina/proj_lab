from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from app.prioritization import *

from app import app, db
from app.model import Pasutijums, Darbinieki
from sqlalchemy import not_, desc, or_
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

@app.route('/prioritizet', methods=['POST'])
def prioritizet():
    try:
        orders = Pasutijums.query.all()
        if orders:
            queue_priority_calculation(orders)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Status updated successfully'})
        else:
            return jsonify({'success': False, 'message': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error updating status: {e}")
        return f"Error: {e}", 400

    finally:
        db.session.close()



@app.route('/ielogosanas')
def ielogosanas():
    return render_template('ielogosanas.html')

@app.route('/adminmain')
def adminmain():
    # all_orders = Pasutijums.query.filter(Pasutijums.materiala_statuss.isnot('Gaida piegādi')).all()
    all_orders = (
    Pasutijums.query
        .filter(or_(
            Pasutijums.kopejais_statuss == 'Gaida rindā',
            Pasutijums.kopejais_statuss == 'Gaida materiālus',
            Pasutijums.kopejais_statuss == '',
            Pasutijums.kopejais_statuss.is_(None),
        ))
        .order_by(desc(Pasutijums.vieta_rinda))
        .all()
)

    available_order = Pasutijums.query.filter_by(kopejais_statuss='Gaida rindā') \
    .order_by(desc(Pasutijums.vieta_rinda)) \
    .first()
    wait_del = (
        Pasutijums.query
        .filter(or_(
        Pasutijums.kopejais_statuss == 'Printēšana pabeigta',
        Pasutijums.kopejais_statuss == 'Aizsūtīts',
        Pasutijums.kopejais_statuss == 'Pabeigts',
    ))
    ).all()
    return render_template(
        'adminmain.html',
        orders=all_orders,
        available_order=available_order,
        wait_del=wait_del,
    )


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
        order_id = request.form.get('id')  # Получаем ID заказа
        new_status = (request.form.get('status'))  # Получаем новый статус

        # Находим заказ по ID и обновляем его статус
        order = Pasutijums.query.get(order_id)
        if order:
            order.materiala_statuss = new_status
            db.session.commit()
            return jsonify({'success': True, 'message': 'Status updated successfully'})
        else:
            return jsonify({'success': False, 'message': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error updating status: {e}")
        return f"Error: {e}", 400

    finally:
        db.session.close()

@app.route('/update_full_status', methods=['POST'])
def update_full_status():
    try:
        order_id = request.form.get('id')  # Получаем ID заказа
        new_full_status = request.form.get('kopejaisSatuss')  # Получаем новый статус
        order = Pasutijums.query.get(order_id)
        if order:
            order.kopejais_statuss = new_full_status
            db.session.commit()
            return jsonify({'success': True, 'message': 'Status updated successfully'})
        else:
            return jsonify({'success': False, 'message': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error updating status: {e}")
        return f"Error: {e}", 400

    finally:
        db.session.close()
        
@app.route('/update_status_waiting', methods=['POST'])
def update_status_waiting():
    try:
        order_id = request.form.get('id')  # Получаем ID заказа
        vai_gaidija = bool(int(request.form.get('gaidija_materialus')))  # Получаем новый статус

        # Находим заказ по ID и обновляем его статус
        order = Pasutijums.query.get(order_id)
        if order:
            order.gaidija_materialus = vai_gaidija
            db.session.commit()
            return jsonify({'success': True, 'message': 'Status updated successfully'})
        else:
            return jsonify({'success': False, 'message': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

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
        kopejais_statuss = ''
        darba_apjoms = work_volume_calculation(izmers, int(daudzums))
        vieta_rinda = -1
        gaidija_materialus = None

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
            materiala_statuss=materiala_statuss,
            kopejais_statuss=kopejais_statuss,
            darba_apjoms=darba_apjoms,
            vieta_rinda=vieta_rinda,
            gaidija_materialus=gaidija_materialus
        )
        
        
        db.session.add(new_order)
        db.session.commit()
        # queue_priority_calculation()

        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error: {e}")
        return f"Error: {e}", 400

    finally:
        db.session.close()