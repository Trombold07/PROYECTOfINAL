# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Control(models.Model):
    _name = 'silabos.control'
    _description="Esta Clase almacena el Control diario de la Asignatura"
    name = fields.Char('Nombre del Control')

    fecha=fields.Date('Fecha de la Clase')
    tema_dictado=fields.Char('Tema Dictado')
    actividades=fields.Char('Actividades')
    recursos=fields.Char('Recursos Utilizados')
    estudiante_id = fields.Many2one('silabos.estudiante', 'Estudiante Delegado')
    observacion=fields.Html('Observaciones del Estudiante')
    semana_id = fields.Many2one('silabos.semana', 'Agregar Semana')
    planificacion_id = fields.Many2one('silabos.Planificacion', 'Agregar Planificacion')


