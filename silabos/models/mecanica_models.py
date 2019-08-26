from odoo import models, fields, api
class mecanica(models.Model):
    _name = 'silabos.mecanica'
    _description="Esta Clase enlista las Mecanicas"

    nombre= fields.Char('Nombre de la Mecanica')
    direccion= fields.Char('Direccion de la Mecanica ')
    telefono=fields.Char('telefono de la Mecanica')
    horarioatencion=fields.Char('Horario de Atencion de la Mecanica')
