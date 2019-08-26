# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Unidad(models.Model):
    _name = 'silabos.unidad'
    _description ="Esta Clase almacena las Unidades de una Asignatura"

    def name_get(self):
        return [(rec.id,rec.nombre+'')for rec in self]


    nombre = fields.Char('Nombre de la Unidad')

    resultadoAprendizaje = fields.Html('Resultado de Aprendizaje de la Unidad')
    metoAprendizaje = fields.Html('Metodologia de Aprendizaje')
    recDidacticos = fields.Html('Recursos Didacticos')

    semana_ids=fields.One2many('silabos.semana', 'unidad_id', string="Semana")

    silabo_id= fields.Many2one('silabos.silabo', "Agregar Silabo")
    asignatura_id = fields.Many2one('silabos.asignatura', "Agregar Asignatura")
    contenido_ids = fields.One2many('silabos.contenido', 'unidad_id', string="Temas  a Impartir Durante la Unidad")
