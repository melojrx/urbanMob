from app import db
from ..user.models.userModels import User
from .loginRouts import login_bp
from flask_login import login_user, logout_user
from flask import render_template, request, redirect, url_for

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template('register.html')

#@login_bp.route('/')
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('/listar')) 
        #return redirect("/listar")
        #return render_template('home.html')
    else:
        return render_template('login.html')

@login_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))