import math
import datetime
# import sys
# sys.path.append('C:/Users/Banknote/Documents/GitHub/proj_lab')
from app import app, db
from app.model import Pasutijums

def work_volume_calculation(paper_size_str, paper_count):
    # Расчет приоритета на основе размера бумаги и объема работы. Предполагается, что, для работы с большим листом будет больше работы.
    # Отношения: 1xA0 = 2xA1 = 4xA2 = 8xA3..... = 10 единица обьема работы
    paper_size = int(paper_size_str[1])
    return (paper_count / (2 ** paper_size))*10

def queue_priority_calculation():
    try:
        # Получаем все заказы из базы данных
        orders = Pasutijums.query.all()  # Возвращает все записи из таблицы "Pasutijums"

        # Проходим по каждому заказу в базе данных
        for order in orders:
            # Извлекаем нужную информацию
            materiala_statuss = order.materiala_statuss
            
            izveides_laiks_str = order.IzveidotsLaiks
            izveides_laiks = datetime.datetime.strptime(izveides_laiks_str, "%Y-%m-%d %H:%M:%S")
            today = datetime.datetime.now()
            starpiba = today - izveides_laiks
            gaidisanas_laiks = int(starpiba.days)
            
            darba_apjoms = order.darba_apjoms
            
            if materiala_statuss != 'Ir pieejams':
                continue 
            else:
                order.vieta_rinda = darba_apjoms**(-1) * gaidisanas_laiks
            
            db.session.commit()  # Сохраняем все изменения в базе данных

        return "Orders processed successfully"
    except Exception as e:
        db.session.rollback()  # Откатываем изменения в случае ошибки
        return f"Error occurred: {e}"
    


    
