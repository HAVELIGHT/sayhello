import os
from sayhello import app


dev_db="mysql+pymysql://root:root@9824fdc85d37.c.staros.cloud:33649/sayhello?charset=utf8"
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
BOOTSTRAP_SERVE_LOCAL=True


