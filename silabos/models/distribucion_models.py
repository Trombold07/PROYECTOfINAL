# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Semana(models.Model):
    _name = 'silabos.distribucion'
    _description="Esta Clase almacena la Distribucion de las Horasde Conformidad cn el Art 15 del RRA"

    horasTeoriXDocente = fields.Integer('Horas Teoricas Asistidas por el Docente')
    porcenhorasTeoriXDocente = fields.Selection([
        ('5%', '5%'),
        ('10%', '10%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
    ], string="Porcentaje Horas Teoricas Asistidas por el Docente")
    horasPractiXDocente = fields.Integer('Horas Practicas Asistidas por el Docente')

    porcenhorasPractiXDocente = fields.Selection([
        ('5%', '5%'),
        ('10%', '10%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
    ], string="Porcentaje Horas Practicas Asistidas por el Docente")

    virtual = fields.Integer('Virtual')
    porcenhorasVirtuales = fields.Selection([
        ('5%', '5%'),
        ('10%', '10%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
    ], string="Porcentaje Virtual")
    presencial = fields.Integer('Presencial')
    porcenPresencial = fields.Selection([
        ('5%', '5%'),
        ('10%', '10%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
    ], string="Porcentaje Horas Presencial")
    horasPractiCampoTalle=fields.Integer(" Horas de Practica del Campo, Talleres")
    porcenhorasPractiCampoTalle = fields.Selection([
        ('5%', '5%'),
        ('10%', '10%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
    ], string="Porcentaje Horas Practicas de Campo Talleres")

    hrsTrabAuto = fields.Integer("Horas de Trabajo Autonomo")
    porcenhrsTrabAuto = fields.Selection([
        ('5%', '5%'),
        ('10%', '10%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
    ], string="Porcentaje Horas Trabajo Autonomo")

    #silabo_id = fields.Many2one('silabos.silabo', "Silabo")


