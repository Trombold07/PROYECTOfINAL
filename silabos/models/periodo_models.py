# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Periodo(models.Model):
    _name = 'silabos.periodo'
    _description ="Esta Clase almacena el Periodo Academico "

    name = fields.Char('Periodo Academico')

    fecha_inicio = fields.Date('Fecha de Inicio del Periodo Academico')
    fecha_fin = fields.Date('Fecha Fin del Periodo Academico')
    carrera_ids = fields.One2many('silabos.carrera', 'periodo_id', string="Carreras")