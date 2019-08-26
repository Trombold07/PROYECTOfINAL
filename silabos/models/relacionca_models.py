# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Relacionca(models.Model):
    _name = 'silabos.relacionca'
    _description = "Esta Clase almacena la relacion de los contenidos de la asignatura con los resultadps de aprendizaje"

    contenido = fields.Char('CONTENIDOS DE LA ASIGNATURA')

    contribucion = fields.Selection([
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ], string="Contribucion")
    resultado = fields.Char('#Resultado de Aprendizaje')
    silabo_id= fields.Many2one('silabos.silabo', "Agregar Silabo")