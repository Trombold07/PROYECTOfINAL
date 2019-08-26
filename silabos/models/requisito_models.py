# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Requisito(models.Model):
    _name = 'silabos.requisito'
    _description="Esta Clase almacena los requisitos de las asignaturas"


    prerequisito= fields.Char(' Asignaturas Prerequisito')
    codigo_prerequisito= fields.Char('Codigo ')
    corequisito = fields.Char('Asignatura  Correquisitos ')
    codigo_corequisito = fields.Char('Codigo')
    asignatura_id =fields.Many2one('silabos.asignatura', 'Agregar Asignatura')
    silabo_id = fields.Many2one('silabos.silabo', "Agregar Silabo")