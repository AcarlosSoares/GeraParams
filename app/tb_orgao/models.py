# coding: utf-8

from flask import current_app
from app import db


class Orgao(db.Model):

    __tablename__ = 'tb_orgao'

    id_orgao= db.Column('id_orgao', db.Integer, primary_key=True)
    dsc_orgao= db.Column('dsc_orgao', db.String(60), nullable=False)
