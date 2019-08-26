# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Criterio(models.Model):
    _name = 'silabos.criterio'
    _description="Esta Clase almacena los Criterios de Evaluacion del estudiante por Resultados de Aprendizaje"


    instrumento= fields.Char('Intrumentos')


    porcentaje1 = fields.Integer("Porcentaje Primer Parcial %")


    puntos1 = fields.Integer("Puntos Primer Parcial")
    porcentaje2 = fields.Integer("Porcentaje Segundo Parcial %")

    puntos2 = fields.Integer("Puntos Segundo Parcial")

    silabo_id = fields.Many2one('silabos.silabo', 'Silabo')
