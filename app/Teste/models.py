# coding: utf-8

from flask import current_app
from app import db


class Teste(db.Model):

    __tablename__ = 'Teste'

    id_empresa= db.Column('id_empresa', db.Integer, primary_key=True)
    ds_nomefantasia_emp= db.Column('ds_nomefantasia_emp', db.String(10), nullable=False)
    ds_razaosocial_emp= db.Column('ds_razaosocial_emp', db.String(10), nullable=False)
    ds_cnpj_emp= db.Column('ds_cnpj_emp', db.String(10), nullable=False)
    ds_cidade_emp= db.Column('ds_cidade_emp', db.String(10), nullable=False)
