from app import db

class Pasutijums(db.Model):
    __tablename__ = 'pasutijums'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Добавьте autoincrement=True
    vards = db.Column(db.String(50), nullable=False)
    uzvards = db.Column(db.String(50), nullable=False)
    TelefonaNumurs = db.Column(db.String(20), nullable=False)
    epasts = db.Column(db.String(120), nullable=False)
    PiegadesAdrese = db.Column(db.String(255), nullable=False)
    izmers = db.Column(db.String(50), nullable=False)
    daudzums = db.Column(db.Integer, nullable=False)
    komentari = db.Column(db.Text)
    FailaAugšupielāde = db.Column(db.String(255))
    IzveidotsLaiks = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Pasutijums {self.vards} {self.uzvards}>'