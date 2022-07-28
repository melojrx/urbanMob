from flask import render_template
from ..rotas.userRout import user_bp
from ..models.userModel import User

@user_bp.route('/listar', methods=['GET', 'POST'])
def listUsers():
    users = User.query.all()
    return render_template('list.html', users=users)