# coding: utf-8

from flask import current_app
from app import db


class @@TABLE_MODEL@@(db.Model):

    __tablename__ = '@@TABLE_NAME@@'

    @@MODELS_ATTR@@
