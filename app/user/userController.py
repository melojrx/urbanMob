from app import app
from flask import Blueprint
from flask import render_template
from userRout import user_bp
from user.models.userModels import User

@user_bp.route('/listar', methods=['GET', 'POST'])
def listUsers(self):
    users = User.query.all()
    return render_template('list.html', users=users)