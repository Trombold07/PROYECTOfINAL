# -*- coding: utf-8 -*-
from odoo import models, fields, api
class MallaCurricular(models.Model):
    _name = 'silabos.malla_curricular'
    _description="Esta Clase almacena la malla Curricular de las Carreras de ITSLA"

    name = fields.Char('Nombre de la Malla Curricular')

    nro_asignaturas = fields.Integer('Numero de Asignaturas de la Malla Curricular')

