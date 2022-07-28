import datetime

from flask_login import current_user
from ..database import db
from ..enum import statusEventoEnum
from ..models.eventoModel import Evento
from ..models.categoriaModel import Categoria
from ..models.subcategoriaModel import Subcategoria
from app.models.eventoHistoricoModel import EventoHistorico
from ..rotas.eventoRout import evento_bp
from flask import jsonify, render_template, request, redirect, session, url_for

class eventoController:

    @evento_bp.route('/evento', methods=['GET'])
    def iniciar():
        listCategoria =  Categoria.query.filter(Categoria.dataFim.is_(None)).all()
        return render_template('cadastrarEvento.html', listCategoria=listCategoria)

    @evento_bp.route('/cadastrar' , methods=['POST'])
    def cadastrar():

        subcategoriaSelect = request.form['subcategoria']
        txtProblema = request.form['txtProblema']
        dataInicio = datetime.datetime.now()

        evento = Evento(subcategoriaSelect, txtProblema, dataInicio)
        eventoHistorico= EventoHistorico(evento, statusEventoEnum.StatusEventoEnum.STATUS_1.value, current_user.id, dataInicio)

        db.session.add(eventoHistorico)
        db.session.commit()

        return redirect(url_for('evento.iniciar'))

    @evento_bp.route('/listar', methods=['GET', 'POST'])
    def listar():
        listEvento = Evento.query.all()
        return render_template('listarEventos.html', listEvento=listEvento)

    # https://tutorial101.blogspot.com/2021/01/python-flask-dynamic-loading-of.html
    @evento_bp.route("/loadSubcategoria",methods=["POST","GET"])
    def loadSubcategoria():
  
        if request.method == 'POST':
            category_id = request.form['parent_id']
            listSubcategoria = Subcategoria.query.filter(Subcategoria.idCategoria == category_id).all()
        return jsonify({'htmlresponse': render_template('subcategoriaAjax.html', listSubcategoria=listSubcategoria)})     