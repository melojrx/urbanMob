from flask import Blueprint, Flask, redirect, render_template, url_for
from flask_login import LoginManager


public = Blueprint('public', __name__)
@public.route('/')
def home():
        return redirect(url_for('login.login'))


app = Flask(__name__)

login_manager = LoginManager(app)

from .blueprints.loginRout import login_bp
from .blueprints.userRout import user_bp
from .blueprints.eventoRout import evento_bp

app.register_blueprint(public)
app.register_blueprint(login_bp)
app.register_blueprint(user_bp)
app.register_blueprint(evento_bp)
print(list(app.url_map.iter_rules()))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SECRET_KEY'] = 'secret'

