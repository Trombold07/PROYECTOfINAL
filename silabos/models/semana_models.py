# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Semana(models.Model):
    _name = 'silabos.semana'
    _description="Esta Clase almacena las semanas que tiene una Unidad de una Asignatura"

    name = fields.Char('Nombre de la Semana')

    fechaInicio= fields.Date('Fecha Inicio de  Semana')
    fechaFin = fields.Date('Fecha Finalización de  Semana')
    horas_duracion= fields.Integer('Número de Horas de la Semana de la  Unidad')
    contenido = fields.Html('Contenidos y Actividades de Estudio Teórico')
    actividades_practicas = fields.Html('¿Qué Actividades Prácticas se Realizarán?')
    trabajo_autonomo = fields.Html('¿Qué Actividades de Trabajo Autónomo se Realizarán?')
    escenario = fields.Html('¿En qué Escenario de Aprendizaje se Realizarán?')

    planificacion_ids = fields.One2many('silabos.planificacion', 'semana_id', string="Planificacion Diaria")

    unidad_id = fields.Many2one('silabos.unidad', 'Agregar Unidad')


    silabo_id= fields.Many2one('silabos.silabo', "Agregar Silabo")

