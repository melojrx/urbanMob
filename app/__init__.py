from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask import Blueprint, Flask, redirect, url_for


public = Blueprint('public', __name__)
@public.route('/')
def home():
        return redirect(url_for('login.login'))


app = Flask(__name__)
Bootstrap(app)

login_manager = LoginManager(app)

from .rotas.loginRout import login_bp
from .rotas.eventoRout import evento_bp

app.register_blueprint(public)
app.register_blueprint(login_bp)
app.register_blueprint(evento_bp)
#print(list(app.url_map.iter_rules()))

