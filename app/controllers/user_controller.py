from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db
from app.models import user_models
from ..models.user_models import User 

@app.route('/')
def home():
    # return redirect(url_for('login')) 
    return redirect('/login')
    # return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        print('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
        login_user(user)
        print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        # return redirect(url_for('home'))
        return render_template('home.html')
    else:
        print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
        return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)

    
