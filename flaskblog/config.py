import os


class Config:
    SECRET_KEY = 'febca97ddb36cf1f8b5770038a14b3e4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'donish.studio@gmail.com'
    MAIL_PASSWORD = '2843406aA'