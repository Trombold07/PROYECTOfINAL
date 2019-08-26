from odoo import models, fields, api
class mecanico(models.Model):
    _name = 'silabos.mecanico'
    _description="Esta Clase almacena los Mecanicos en Servicio"

    name= fields.Char('Nombres y Apellidos del Mecanico')
    id= fields.Char('ID del Mecanico ')
    direccion=fields.Char('Direccion de la Mecanica')
    telefono= fields.Char('Telefono del Mecanico ')

