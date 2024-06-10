from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    pigs = db.relationship('Pig', backref='owner', lazy=True)

class Pig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    health_records = db.relationship('HealthRecord', backref='pig', lazy=True)
    feed_records = db.relationship('FeedRecord', backref='pig', lazy=True)

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pig_id = db.Column(db.Integer, db.ForeignKey('pig.id'), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    diagnosis = db.Column(db.String(120), nullable=False)
    treatment = db.Column(db.Text, nullable=False)

class FeedRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pig_id = db.Column(db.Integer, db.ForeignKey('pig.id'), nullable=False)
    feed_type = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    treatment = db.Column(db.Text, nullable=False)