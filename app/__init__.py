from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .login.loginRouts import login_bp
from .user.userRout import user_bp

app = Flask(__name__)
app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)

app.register_blueprint(login_bp)
app.register_blueprint(user_bp)
app.add_url_rule('/', endpoint='login')


# @app.route('/')
# def home():
#     print('ascavsavd')
#     return redirect(url_for('login'))
#     #return redirect('/login')