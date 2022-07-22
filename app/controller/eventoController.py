from sqlalchemy import null
from ..database import db
from ..models.categoriaModel import Categoria
from ..blueprints.eventoRout import evento_bp
from flask import render_template, request, redirect, url_for

class eventoController:

    @evento_bp.route('/evento', methods=['GET'])
    def iniciar():

        #listCategoria = Categoria.query.where(Categoria.datFim == null).all()
        listCategoria = Categoria.query.all()

        return render_template('cadastrarEvento.html', listCategoria=listCategoria)


    @evento_bp.route('/cadastrar' , methods=['POST'])
    def cadastrar():
        select = request.form.get('categoria')
        print(select)
        return redirect(url_for('evento.iniciar'))

