from msilib import schema
from ..database import db

class Evento(db.Model):
    __tablename__ = 'tb_evento_eve'
    __table_args__ = {"schema":"cidade"}
    
    id = db.Column('id_evento_eve', db.Integer, autoincrement=True, primary_key=True)
    idSubcategoria = db.Column('id_subcategoria_eve',db.Integer, db.ForeignKey('cidade.tb_subcategoria_sub.id_subcategoria_sub'), nullable=False)
    txtProblema = db.Column('txt_problema_eve', db.String(1000), nullable=False)
    dataInicio = db.Column('dat_inicio_eve', db.DateTime, nullable=False)
    dataFim = db.Column('dat_fim_eve', db.DateTime, nullable=True)


    def __init__(self, idSubcategoria, txtProblema, dataInicio, dataFim):
        self.idSubcategoria = idSubcategoria
        self.txtProblema = txtProblema
        self.dataInicio = dataInicio
        self.dataFim = dataFim