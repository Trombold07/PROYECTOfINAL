from odoo import models, fields, api
class vehiculo(models.Model):
    _name = 'silabos.vehiculo'
    _description="Esta Clase almacena los Vehiculos"

    marca= fields.Char('Marca del vehiculo')
    placa= fields.Char('Placa del vehiculo ')
    estadovehiculo=fields.Html('Estado del vehiculo')