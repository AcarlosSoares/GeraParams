# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired, ValidationError
from app.@@TABLE_NAME@@.models import @@TABLE_MODEL@@

ordenarpor_choices=[@@ORDENARPOR_CHOICES@@]
ordem_choices=[('ASC', 'Asc'), ('DESC', 'Desc')]


class ListaForm(FlaskForm):
  ordenarpor = SelectField('Ordenar Por', choices=ordenarpor_choices)
  ordem = SelectField('Ordem', choices=ordem_choices)
  pesquisarpor = StringField('Filtrar Por')
  submit_enviar = SubmitField('Enviar')
  submit_limpar = SubmitField('Limpar')


class IncluiForm(FlaskForm):
  @@INSERT_FORM@@
  submit = SubmitField('Enviar')


class AlteraForm(FlaskForm):
  @@UPDATE_FORM@@
  submit = SubmitField('Enviar')

