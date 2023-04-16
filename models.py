from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)