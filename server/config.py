import os
from datetime import timedelta

class Config:
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://eddie:zeddie20062306@localhost:5432/late_show_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'change-this-in-production'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-secret-in-production'
    DEBUG = True
