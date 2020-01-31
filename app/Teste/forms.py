# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired, ValidationError
from app.Teste.models import Teste

ordenarpor_choices=[('Teste.id_empresa','Nome Fantasia'),('Teste.ds_nomefantasia_emp','Razã£O Social'),('Teste.ds_razaosocial_emp','Cnpj')]
ordem_choices=[('ASC', 'Asc'), ('DESC', 'Desc')]


class ListaForm(FlaskForm):
  ordenarpor = SelectField('Ordenar Por', choices=ordenarpor_choices)
  ordem = SelectField('Ordem', choices=ordem_choices)
  pesquisarpor = StringField('Filtrar Por')
  submit_enviar = SubmitField('Enviar')
  submit_limpar = SubmitField('Limpar')


class IncluiForm(FlaskForm):
  ds_nomefantasia_emp = StringField('Nome Fantasia', validators=[DataRequired()])
  ds_razaosocial_emp = StringField('RazÃ£o Social', validators=[DataRequired()])
  ds_cnpj_emp = StringField('CNPJ', validators=[DataRequired()])
  ds_cidade_emp = StringField('Cidade', validators=[DataRequired()])
  submit = SubmitField('Enviar')


class AlteraForm(FlaskForm):
  ds_nomefantasia_emp = StringField('Nome Fantasia', validators=[DataRequired()])
  ds_cnpj_emp = StringField('CNPJ', validators=[DataRequired()])
  ds_cidade_emp = StringField('Cidade', validators=[DataRequired()])
  submit = SubmitField('Enviar')

