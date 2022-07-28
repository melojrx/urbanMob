import datetime
from ..database import db
from sqlalchemy import null
from sqlalchemy import insert
from ..models.eventoModel import Evento
from ..models.categoriaModel import Categoria
from ..models.subcategoriaModel import Subcategoria
from ..blueprints.eventoRout import evento_bp
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

        # values = {"id_subcategoria_eve": subcategoriaSelect, "txt_problema_eve": txtProblema, "dat_inicio_eve": dataInicio}
        #db.session.execute(Evento.__table__.insert().values(values))
        # db.session.commit()

        evento = Evento(subcategoriaSelect, txtProblema, dataInicio)
        db.session.add(evento)
        db.session.commit()

        return redirect(url_for('evento.iniciar'))

    # https://tutorial101.blogspot.com/2021/01/python-flask-dynamic-loading-of.html
    @evento_bp.route("/loadSubcategoria",methods=["POST","GET"])
    def loadSubcategoria():
  
        if request.method == 'POST':
            category_id = request.form['parent_id']
            listSubcategoria = Subcategoria.query.filter(Subcategoria.idCategoria == category_id).all()
        return jsonify({'htmlresponse': render_template('subcategoriaAjax.html', listSubcategoria=listSubcategoria)})     