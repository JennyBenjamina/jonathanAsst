from app import db

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    knowledge = db.Column(db.String(20000))
