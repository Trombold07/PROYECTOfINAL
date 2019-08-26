from odoo import models, fields, api
class mantenimiento(models.Model):
    _name = 'silabos.mantenimiento'
    _description="Esta Clase enlista Mantenimientos"

    tipo= fields.Char('Mantenimiento')
    fechainicio= fields.Date('Fecha de inicio del Mantenimiento ')
    fechafin=fields.Date('Fecha final del Mantenimiento')
    descripcion=fields.Html('Descripcion del mantenimiento')