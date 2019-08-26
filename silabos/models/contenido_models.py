# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Contenido(models.Model):
    _name = 'silabos.contenido'
    _description ="Esta Clase almacena los Contenidos de cada Unidad"

    unidad = fields.Selection([
        ('unidad1', 'Unidad 1'),
        ('unidad2', 'Unidad 2'),
        ('unidad3', 'Unidad 3'),

    ])
    tema = fields.Char('TEMA/ CONTENIDO')
    teoricas = fields.Integer('#Horas Teoricas')
    practicas = fields.Integer('#Horas Practicas')
    tutorias = fields.Integer('#Horas de Tutorias')
    actPractica = fields.Integer('#Horas de Actividades  de Practica')
    tautonomo = fields.Integer('#Horas de Actividades de trabajo Autónomo')
    mecanismoEva = fields.Char('Mecanismo de Evaluación')
    unidad_id = fields.Many2one('silabos.unidad', ' UNIDAD')
    bibliografia_ids = fields.One2many('silabos.bibliografia', 'contenido_id', string="Bibliografia")
    silabo_id = fields.Many2one('silabos.silabo', "Agregar Silabo")