import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Denice:TestSubject.1010@localhost/ophmfas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
