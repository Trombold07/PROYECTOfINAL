# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Ciclo(models.Model):
    _name = 'silabos.ciclo'
    _description ="Esta Clase almacena el El ciclo de la Carrera "

    def name_get(self):
        # para iniciar el debug
        # pdb.set_trace()
        return [(rec.id, rec.nombre + '') for rec in self]
    nombre = fields.Char(' Nombre Ciclo Academico')
    carrera_id = fields.Many2one('silabos.carrera', 'Agregar Carrera')
    asignatura_ids = fields.One2many('silabos.asignatura', 'ciclo_id', string=" Asignatura")
