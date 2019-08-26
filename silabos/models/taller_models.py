from odoo import models, fields, api
class taller(models.Model):
    _name = 'silabos.taller'
    _description="Esta Clase almacena el numero de talleres de la mecanica"

    numerotaller= fields.Integer('Numero de taller')
    capacidad= fields.Integer('Capacidad del Taller ')

