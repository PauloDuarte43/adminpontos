# -*- encoding: utf-8 -*-

#  python imports
import os

#  Flask imports
from flask import Flask
from flask import redirect

#  third party imports
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth

#  app imports

app = Flask(__name__)


# Configurations
app.config.from_object('admin.configs.config')

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

if not os.getenv('ADMIN_PONTOS_USER'):
    raise Exception()

if not os.getenv('ADMIN_PONTOS_PASS'):
    raise Exception()

app.config['BASIC_AUTH_USERNAME'] = os.getenv('ADMIN_PONTOS_USER') 
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('ADMIN_PONTOS_PASS')
app.config['BASIC_AUTH_FORCE'] = True

db = SQLAlchemy(app)

basic_auth = BasicAuth(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    nome = db.Column(db.String(255), default='')
    pontos = db.Column(db.Integer, default=20)
    pontos_pro = db.Column(db.Integer, default=20)
    motivos = db.Column(db.String(5000), default='')
    
    def __repr__(self):
        return '<User %r:%r>' % (self.id, self.email)

admin = Admin(app, name='pontos', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))


@app.route('/')
def hello():
    return redirect('http://projetos.pauloroger.tk/pontos')
