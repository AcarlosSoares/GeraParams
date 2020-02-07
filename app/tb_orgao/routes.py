# coding: utf-8

from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, make_response)
from flask_login import current_user, login_required
from sqlalchemy import desc, asc, text
from app import db
from app.tb_orgao.models import Orgao
from app.tb_orgao.forms import ListaForm, IncluiForm, AlteraForm
import os

tb_orgao = Blueprint('tb_orgao', __name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))


@tb_orgao.route('/tb_orgao/acessar', methods=['GET', 'POST'])
@login_required
def tb_orgao_acessar():

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  form = ListaForm()

  ordenarpor = request.form.get('ordenarpor')
  ordem = request.form.get('ordem')
  pesquisarpor = request.form.get('pesquisarpor')
  imprimir = request.form.get('imprimir')

  if imprimir:
    response = tb_orgao_imprimir()
    return response

  limpar = request.form.get('submit_limpar')
  if limpar:
    form.ordenarpor.data = 'tb_orgao.id_orgao'
    form.ordenarpor.data = 'ASC'
    form.ordenarpor.data = None
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  try:
    page = request.form.get('page', 1, type=int)
    if ordenarpor and ordem and pesquisarpor:
      order_column = text(ordenarpor + ' ' + ordem)
      filter_column = text(ordenarpor + ' LIKE ' + "'%" + pesquisarpor + "%'")
      dados = Orgao.query.order_by(order_column).filter(filter_column).paginate(page=page, per_page=8)
    elif ordenarpor and ordem:
      order_column = text(ordenarpor + ' ' + ordem)
      dados = Orgao.query.order_by(order_column).paginate(page=page, per_page=8)
    else:
      dados = Orgao.query.paginate(page=page, per_page=8)
    return render_template('tb_orgao_lista.html', title='Lista de Orgao', dados=dados, form=form)
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('users.logout'))


@tb_orgao.route('/tb_orgao/incluir', methods=['GET', 'POST'])
@login_required
def tb_orgao_incluir():

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  form = IncluiForm()

  if request.method == 'GET':
    return render_template('tb_orgao_inclui.html', title='Incluir Orgao', form=form)

  if not form.validate_on_submit():
    flash('Formulário não validado!', 'info')
    return render_template('tb_orgao_inclui.html', title='Incluir Orgao', form=form)

  if form.validate_on_submit():
    try:
      dado = Orgao(id_orgao=form.id_orgao.data, dsc_orgao=form.dsc_orgao.data)
      db.session.add(dado)
      db.session.commit()
      flash('Registro foi incluído com sucesso!', 'success')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))


@tb_orgao.route("/tb_orgao/excluir/<int:id_data>", methods=['POST'])
@login_required
def tb_orgao_excluir(id_data):

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  try:
    dado = Orgao.query.get(id_data)
    if dado:
      db.session.delete(dado)
      db.session.commit()
      flash('Registro foi excluido com sucesso!', 'success')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))
    else:
      flash('Falha na exclusão!', 'danger')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))


@tb_orgao.route('/tb_orgao/alterar/<int:id_data>', methods=['GET', 'POST'])
@login_required
def tb_orgao_alterar(id_data):

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  form = AlteraForm()

  if request.method == 'GET':
    try:
      dado = Orgao.query.get(id_data)
      form.id_orgao.data = dado.id_orgao
      form.dsc_orgao.data = dado.dsc_orgao
      return render_template('tb_orgao_altera.html', title='Alterar Orgao', form=form)
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  if not form.validate_on_submit():
    flash('Formulário não validado!', 'info')
    return render_template('tb_orgao_altera.html', title='Alterar Orgao', form=form)

  if form.validate_on_submit():
    try:
      dado = Orgao.query.get(id_data)
      dado.id_orgao = form.id_orgao.data
      dado.dsc_orgao = form.dsc_orgao.data
      db.session.commit()
      flash('Registro foi alterado com sucesso!', 'success')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('tb_orgao.tb_orgao_acessar'))


def tb_orgao_imprimir():

  from app_modelo.principal.relatorios import imprimir_reportlab

  ordenarpor = request.form.get('ordenarpor')
  ordem = request.form.get('ordem')
  pesquisarpor = request.form.get('pesquisarpor')

  # LÊ BASE DE DADOS
  try:
    if ordenarpor and ordem and pesquisarpor:
      order_column = text(ordenarpor + ' ' + ordem)
      filter_column = text(ordenarpor + ' LIKE ' + "'%" + pesquisarpor + "%'")
      dados = Orgao.query.order_by(order_column).filter(filter_column).all()
    elif ordenarpor and ordem:
      order_column = text(ordenarpor + ' ' + ordem)
      dados = Orgao.query.order_by(order_column).all()
    else:
      dados = Orgao.query.all()
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('tb_orgao.tb_orgao_acessar'))

  # # # PARÂMETROS DO RELATÓRIO
  titulo = 'LISTA DE Orgao'.upper()
  subtitulo = None
  lista = [
    ['Seq', 'row.id_orgao', 50, 60],
    ['Descricao', 'row.dsc_orgao', 80, 180]
  ]

  response = imprimir_reportlab(titulo, subtitulo, lista, dados)
  return response
