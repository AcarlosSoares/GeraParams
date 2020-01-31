# coding: utf-8

from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, make_response)
from flask_login import current_user, login_required
from sqlalchemy import desc, asc, text
from app import db
from app.@@TABLE_NAME@@.models import @@TABLE_MODEL@@
from app.@@TABLE_NAME@@.forms import @@LIST_FORM@@, @@INSERT_FORM@@, @@UPDATE_FORM@@
import os

@@TABLE_NAME@@ = Blueprint('@@TABLE_NAME@@', __name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))


@@@TABLE_NAME@@.route('/@@TABLE_NAME@@/acessar', methods=['GET', 'POST'])
@login_required
def @@TABLE_NAME@@_acessar():

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  form = @@LIST_FORM@@()

  ordenarpor = request.form.get('ordenarpor')
  ordem = request.form.get('ordem')
  pesquisarpor = request.form.get('pesquisarpor')
  imprimir = request.form.get('imprimir')

  if imprimir:
    response = @@TABLE_NAME@@_imprimir()
    return response

  limpar = request.form.get('submit_limpar')
  if limpar:
    form.ordenarpor.data = '@@TABLE_NAME@@.@@TABLE_PK@@'
    form.ordenarpor.data = 'ASC'
    form.ordenarpor.data = None
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  try:
    page = request.form.get('page', 1, type=int)
    if ordenarpor and ordem and pesquisarpor:
      order_column = text(ordenarpor + ' ' + ordem)
      filter_column = text(ordenarpor + ' LIKE ' + "'%" + pesquisarpor + "%'")
      dados = @@TABLE_MODEL@@.query.order_by(order_column).filter(filter_column).paginate(page=page, per_page=8)
    elif ordenarpor and ordem:
      order_column = text(ordenarpor + ' ' + ordem)
      dados = @@TABLE_MODEL@@.query.order_by(order_column).paginate(page=page, per_page=8)
    else:
      dados = @@TABLE_MODEL@@.query.paginate(page=page, per_page=8)
    return render_template('@@TABLE_NAME@@_lista.html', title='Lista de @@TABLE_MODEL@@', dados=dados, form=form)
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('users.logout'))


@@@TABLE_NAME@@.route('/@@TABLE_NAME@@/incluir', methods=['GET', 'POST'])
@login_required
def @@TABLE_NAME@@_incluir():

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  form = @@INSERT_FORM@@()

  if request.method == 'GET':
    return render_template('@@TABLE_NAME@@_inclui.html', title='Incluir @@TABLE_MODEL@@', form=form)

  if not form.validate_on_submit():
    flash('Formulário não validado!', 'info')
    return render_template('@@TABLE_NAME@@_inclui.html', title='Incluir @@TABLE_MODEL@@', form=form)

  if form.validate_on_submit():
    try:
      dado = @@TABLE_MODEL@@(@@INSERT_SQL@@)
      db.session.add(dado)
      db.session.commit()
      flash('Registro foi incluído com sucesso!', 'success')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))


@@@TABLE_NAME@@.route("/@@TABLE_NAME@@/excluir/<int:id_data>", methods=['POST'])
@login_required
def @@TABLE_NAME@@_excluir(id_data):

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  try:
    dado = @@TABLE_MODEL@@.query.get(id_data)
    if dado:
      db.session.delete(dado)
      db.session.commit()
      flash('Registro foi excluido com sucesso!', 'success')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))
    else:
      flash('Falha na exclusão!', 'danger')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))


@@@TABLE_NAME@@.route('/@@TABLE_NAME@@/alterar/<int:id_data>', methods=['GET', 'POST'])
@login_required
def @@TABLE_NAME@@_alterar(id_data):

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  form = @@UPDATE_FORM@@()

  if request.method == 'GET':
    try:
      dado = @@TABLE_MODEL@@.query.get(id_data)
      @@UPDATE_SQL_GET@@
      return render_template('@@TABLE_NAME@@_altera.html', title='Alterar @@TABLE_MODEL@@', form=form)
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  if not form.validate_on_submit():
    flash('Formulário não validado!', 'info')
    return render_template('@@TABLE_NAME@@_altera.html', title='Alterar @@TABLE_MODEL@@', form=form)

  if form.validate_on_submit():
    try:
      dado = @@TABLE_MODEL@@.query.get(id_data)
      @@UPDATE_SQL_POST@@
      db.session.commit()
      flash('Registro foi alterado com sucesso!', 'success')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))


def @@TABLE_NAME@@_imprimir():

  from app_modelo.principal.relatorios import imprimir_reportlab

  ordenarpor = request.form.get('ordenarpor')
  ordem = request.form.get('ordem')
  pesquisarpor = request.form.get('pesquisarpor')

  # LÊ BASE DE DADOS
  try:
    if ordenarpor and ordem and pesquisarpor:
      order_column = text(ordenarpor + ' ' + ordem)
      filter_column = text(ordenarpor + ' LIKE ' + "'%" + pesquisarpor + "%'")
      dados = @@TABLE_MODEL@@.query.order_by(order_column).filter(filter_column).all()
    elif ordenarpor and ordem:
      order_column = text(ordenarpor + ' ' + ordem)
      dados = @@TABLE_MODEL@@.query.order_by(order_column).all()
    else:
      dados = @@TABLE_MODEL@@.query.all()
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('@@TABLE_NAME@@.@@TABLE_NAME@@_acessar'))

  # # # PARÂMETROS DO RELATÓRIO
  titulo = 'LISTA DE @@TABLE_MODEL@@'.upper()
  subtitulo = None
  lista = [
    @@PRINT_LIST@@
  ]

  response = imprimir_reportlab(titulo, subtitulo, lista, dados)
  return response
