from ..database import db

class EventoHistorico(db.Model):
    __tablename__ = 'tb_evento_historico_ehi'
    __table_args__ = {"schema":"cidade"}
    
    id = db.Column('id_evento_historico_ehi', db.Integer, autoincrement=True, primary_key=True)
    idEvento = db.Column('id_evento_ehi',db.Integer, db.ForeignKey('cidade.tb_evento_eve.id_evento_eve'), nullable=False)
    idStatusEvento = db.Column('id_status_evento_ehi', db.Integer, db.ForeignKey('cidade.tb_status_evento_sev.id_status_evento_sev'), nullable=False)
    dataInicio = db.Column('dat_inicio_ehi', db.DateTime, nullable=False)
    dataFim = db.Column('dat_fim_ehi', db.DateTime, nullable=True)

    evento = db.relationship("Evento") 
    statusEvento = db.relationship("StatusEvento")
    
    def __init__(self, evento, idStatusEvento, dataInicio):
        self.evento = evento
        self.idStatusEvento = idStatusEvento
        self.dataInicio = dataInicio