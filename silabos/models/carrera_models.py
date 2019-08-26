# -*- coding: utf-8 -*-
from odoo import models, fields, api
import  pdb
class Carrera(models.Model):
    _name = 'silabos.carrera'
    _description="Esta Clase almacena las Carreras de ITSLA"

    @api.multi

    def name_get(self):
        # para iniciar el debug
        # pdb.set_trace()
        return [(rec.id,rec.nombre+'')for rec in self]


    codigo= fields.Char('Codigo de la Carrera')


    nombre= fields.Char('Nombre de la Carrera')
    periodo_id = fields.Many2one('silabos.periodo', 'Agregar Periodo')
    estudiante_ids = fields.Many2many("silabos.estudiante")
    malla_curricular_id = fields.Many2one('silabos.malla_curricular', 'Agregar Malla Curricular')
    ciclo_ids = fields.One2many('silabos.ciclo', 'carrera_id', string="Ciclos")


