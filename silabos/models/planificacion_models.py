# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Semana(models.Model):
    _name = 'silabos.planificacion'
    _description="Esta Clase almacena la planificación diaria de Clase"



    name = fields.Char('Nombre de la Planificacion')

    horaInicio= fields.Char('Hora Inicio de  Clase')
    horaFin = fields.Char('Hora Inicio de  Clase')

    contenido = fields.Char('Contenidos y Acividades de Estudio Teórico')
    practicas = fields.Char('¿Que actividades Practicas se Realizaran?')
    autonomo = fields.Char('¿Que actividades de trabajo autonomo  se Realizaran?')
    escenario = fields.Char('¿En Que escenario de aprendizaje  se Realizaran?')
    semana_id = fields.Many2one('silabos.semana', 'Agregar Semana')
    control_ids = fields.One2many('silabos.control', 'semana_id', string="Control")
    silabo_id = fields.Many2one('silabos.silabo', "Agregar Silabo")



