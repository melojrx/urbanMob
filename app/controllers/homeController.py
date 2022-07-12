from app import app
from flask import Blueprint
from flask import render_template
from flask_restful import Resource
from app.models.userModels import User

listUsers_bp = Blueprint('listUsers', __name__)

class HomeController(Resource):

    @listUsers_bp.route('/listUsers', methods=['GET', 'POST'])
    def listUsers(self):
        users = User.query.all()
        print('MEU ZOVO')
        return render_template('list.html', users=users)