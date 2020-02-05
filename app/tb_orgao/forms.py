# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired, ValidationError
from app.tb_orgao.models import Orgao

ordenarpor_choices=[('tb_orgao.dsc_orgao','Descricao')]
ordem_choices=[('ASC', 'Asc'), ('DESC', 'Desc')]


class ListaForm(FlaskForm):
  ordenarpor = SelectField('Ordenar Por', choices=ordenarpor_choices)
  ordem = SelectField('Ordem', choices=ordem_choices)
  pesquisarpor = StringField('Filtrar Por')
  submit_enviar = SubmitField('Enviar')
  submit_limpar = SubmitField('Limpar')


class IncluiForm(FlaskForm):
  dsc_orgao = StringField('Descricao', validators=[DataRequired()])
  submit = SubmitField('Enviar')


class AlteraForm(FlaskForm):
  dsc_orgao = StringField('Descricao', validators=[DataRequired()])
  submit = SubmitField('Enviar')

