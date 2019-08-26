# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Resultado(models.Model):
    _name = 'silabos.resultado'
    _description="Esta Clase almacena los resultados  de la  asignatura"



    descripcion=fields.Char('Resultados de Aprendizaje de la Asignatura')
    asignatura_id = fields.Many2one('silabos.asignatura', 'Asignatura')







