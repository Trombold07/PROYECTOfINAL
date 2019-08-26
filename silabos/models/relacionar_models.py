# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Relacionar(models.Model):
    _name = 'silabos.relacionar'
    _description = "Esta Clase almacena la relacion de la Asignatura con Los Resultados de Aprendizaje Del Perfil de Egreso de la Carrera"

    resultados = fields.Char('RESULTADOS DE APRENDIZAJE DE PERFIL DE LA ASIGNATURA')

    contribucion = fields.Selection([
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ], string="CONTRIBUCION AL PERFIL DE EGRESO DE LA CARRERA")
    perfil = fields.Char('PERFIL DE EGRESO DE LA CARRERA')
    silabo_id= fields.Many2one('silabos.silabo', "Agregar Silabo")