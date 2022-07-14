from flask import render_template
from ..blueprints.userRout import user_bp
from .models.userModels import User

@user_bp.route('/listar', methods=['GET', 'POST'])
def listUsers():
    users = User.query.all()
    return render_template('list.html', users=users)