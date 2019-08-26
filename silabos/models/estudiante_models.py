# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Estudiante(models.Model):

    def name_get(self):
        return [(rec.id,rec.nombre+'')for rec in self]

    _name = 'silabos.estudiante'
    _description="Esta Clase almacena los Estudiantes de ITSLA"
    name = fields.Char('Estudiantes')

    cedula= fields.Char('Cedula de Ciudadania')
    nombre = fields.Char('Nombres y Apellidos del Estudiante')
    control_ids = fields.One2many('silabos.control', 'estudiante_id')
    fecha_naciemiento = fields.Date('Fecha de Nacimiento  del Estudiante')
    acta_ids = fields.One2many('silabos.acta', 'estudiante_id')