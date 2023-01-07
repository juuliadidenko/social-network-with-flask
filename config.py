import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    ADMINS = [os.getenv('ADMIN')]
    POSTS_PER_PAGE = 15
    LANGUAGES = ['en', 'ru']
    TRANSLATOR_KEY = os.getenv('TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')
    REDIS_URL = os.getenv('REDIS_URL') or 'redis://'
