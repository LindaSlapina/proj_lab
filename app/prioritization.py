import math
from app import app, db
from app.model import Pasutijums, Darbinieki

def work_volume_calculation(paper_size_str, paper_count):
    # Расчет приоритета на основе размера бумаги и объема работы. Предполагается, что, для работы с большим листом будет больше работы.
    # Отношения: 1xA0 = 2xA1 = 4xA2 = 8xA3..... = 10 единица обьема работы
    paper_size = int(paper_size_str[1])
    return (paper_count / (2 ** paper_size))*10

def queue_priority_calculation():
    
    db.session.commit()
    return 1