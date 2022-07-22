from app import login_manager
from ..database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'tb_usuario_usu'
    __table_args__ = {"schema":"cidade"}
    
    id = db.Column('id_usuario_usu', db.Integer, autoincrement=True, primary_key=True)
    name = db.Column('txt_nome_usu', db.String(200), nullable=False)
    email = db.Column('txt_email_usu', db.String(200), nullable=False, unique=True)
    password = db.Column('txt_password_usu', db.String(128), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)