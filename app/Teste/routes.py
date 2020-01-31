# coding: utf-8

from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, make_response)
from flask_login import current_user, login_required
from sqlalchemy import desc, asc, text
from app import db
from app.Teste.models import Teste
from app.Teste.forms import ListaForm, IncluiForm, AlteraForm
import os

Teste = Blueprint('Teste', __name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))


@Teste.route('/Teste/acessar', methods=['GET', 'POST'])
@login_required
def Teste_acessar():

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('Teste.Teste_acessar'))

  form = ListaForm()

  ordenarpor = request.form.get('ordenarpor')
  ordem = request.form.get('ordem')
  pesquisarpor = request.form.get('pesquisarpor')
  imprimir = request.form.get('imprimir')

  if imprimir:
    response = Teste_imprimir()
    return response

  limpar = request.form.get('submit_limpar')
  if limpar:
    form.ordenarpor.data = 'Teste.id_empresa'
    form.ordenarpor.data = 'ASC'
    form.ordenarpor.data = None
    return redirect(url_for('Teste.Teste_acessar'))

  try:
    page = request.form.get('page', 1, type=int)
    if ordenarpor and ordem and pesquisarpor:
      order_column = text(ordenarpor + ' ' + ordem)
      filter_column = text(ordenarpor + ' LIKE ' + "'%" + pesquisarpor + "%'")
      dados = Teste.query.order_by(order_column).filter(filter_column).paginate(page=page, per_page=8)
    elif ordenarpor and ordem:
      order_column = text(ordenarpor + ' ' + ordem)
      dados = Teste.query.order_by(order_column).paginate(page=page, per_page=8)
    else:
      dados = Teste.query.paginate(page=page, per_page=8)
    return render_template('Teste_lista.html', title='Lista de Teste', dados=dados, form=form)
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('users.logout'))


@Teste.route('/Teste/incluir', methods=['GET', 'POST'])
@login_required
def Teste_incluir():

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('Teste.Teste_acessar'))

  form = IncluiForm()

  if request.method == 'GET':
    return render_template('Teste_inclui.html', title='Incluir Teste', form=form)

  if not form.validate_on_submit():
    flash('Formulário não validado!', 'info')
    return render_template('Teste_inclui.html', title='Incluir Teste', form=form)

  if form.validate_on_submit():
    try:
      dado = Teste(ds_nomefantasia_emp=form.ds_nomefantasia_emp.data, ds_razaosocial_emp=form.ds_razaosocial_emp.data, ds_cnpj_emp=form.ds_cnpj_emp.data, ds_cidade_emp=form.ds_cidade_emp.data)
      db.session.add(dado)
      db.session.commit()
      flash('Registro foi incluído com sucesso!', 'success')
      return redirect(url_for('Teste.Teste_acessar'))
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('Teste.Teste_acessar'))


@Teste.route("/Teste/excluir/<int:id_data>", methods=['POST'])
@login_required
def Teste_excluir(id_data):

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('Teste.Teste_acessar'))

  try:
    dado = Teste.query.get(id_data)
    if dado:
      db.session.delete(dado)
      db.session.commit()
      flash('Registro foi excluido com sucesso!', 'success')
      return redirect(url_for('Teste.Teste_acessar'))
    else:
      flash('Falha na exclusão!', 'danger')
      return redirect(url_for('Teste.Teste_acessar'))
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('Teste.Teste_acessar'))


@Teste.route('/Teste/alterar/<int:id_data>', methods=['GET', 'POST'])
@login_required
def Teste_alterar(id_data):

  if not current_user.is_authenticated:
    flash('Usuário não autorizado!', 'info')
    return redirect(url_for('Teste.Teste_acessar'))

  form = AlteraForm()

  if request.method == 'GET':
    try:
      dado = Teste.query.get(id_data)
      form.ds_nomefantasia_emp.data = dado.ds_nomefantasia_emp
      form.ds_cnpj_emp.data = dado.ds_cnpj_emp
      form.ds_cidade_emp.data = dado.ds_cidade_emp
      return render_template('Teste_altera.html', title='Alterar Teste', form=form)
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('Teste.Teste_acessar'))

  if not form.validate_on_submit():
    flash('Formulário não validado!', 'info')
    return render_template('Teste_altera.html', title='Alterar Teste', form=form)

  if form.validate_on_submit():
    try:
      dado = Teste.query.get(id_data)
      dado.ds_nomefantasia_emp = form.ds_nomefantasia_emp.data
      dado.ds_cnpj_emp = form.ds_cnpj_emp.data
      dado.ds_cidade_emp = form.ds_cidade_emp.data
      db.session.commit()
      flash('Registro foi alterado com sucesso!', 'success')
      return redirect(url_for('Teste.Teste_acessar'))
    except Exception as e:
      flash('Falha no aplicativo! ' + str(e), 'danger')
      return redirect(url_for('Teste.Teste_acessar'))


def Teste_imprimir():

  from app_modelo.principal.relatorios import imprimir_reportlab

  ordenarpor = request.form.get('ordenarpor')
  ordem = request.form.get('ordem')
  pesquisarpor = request.form.get('pesquisarpor')

  # LÊ BASE DE DADOS
  try:
    if ordenarpor and ordem and pesquisarpor:
      order_column = text(ordenarpor + ' ' + ordem)
      filter_column = text(ordenarpor + ' LIKE ' + "'%" + pesquisarpor + "%'")
      dados = Teste.query.order_by(order_column).filter(filter_column).all()
    elif ordenarpor and ordem:
      order_column = text(ordenarpor + ' ' + ordem)
      dados = Teste.query.order_by(order_column).all()
    else:
      dados = Teste.query.all()
  except Exception as e:
    flash('Falha no aplicativo! ' + str(e), 'danger')
    return redirect(url_for('Teste.Teste_acessar'))

  # # # PARÂMETROS DO RELATÓRIO
  titulo = 'LISTA DE Teste'.upper()
  subtitulo = None
  lista = [
    ['Nome Fantasia', 'row.id_empresa', 50, 80],
    ['Razã£O Social', 'row.ds_nomefantasia_emp', 100, 130],
    ['Cnpj', 'row.ds_razaosocial_emp', 150, 180]
  ]

  response = imprimir_reportlab(titulo, subtitulo, lista, dados)
  return response
