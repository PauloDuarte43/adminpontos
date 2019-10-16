# -*- encoding: utf-8 -*-
"""
Módulo com as configurações da APP.
"""
import os
import datetime

# Statement for enabling the development environment
DEBUG = os.getenv('DEBUG', True)

session_life_time_seconds = int(os.getenv('SESSION_LIFE_TIME_SECONDS', 900))
PERMANENT_SESSION_LIFETIME = datetime.timedelta(seconds=session_life_time_seconds)

SQLALCHEMY_DATABASE_URI = 'sqlite:////var/www/paulo/pontos.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Secret key for signing cookies
SECRET_KEY = '\xe2\x1b0\xfe\xe7\x1b\r\x9f\xb0\xb0]\\\xd5\x06\xa0\x16\xd5\xc1\xdf5\x0e\x08h\xcf'

LOG_FILENAME = os.getenv('LOG_FILENAME', '/tmp/adminpontos.log')
LOG_MODE = int(os.getenv('LOG_MODE', 10))
