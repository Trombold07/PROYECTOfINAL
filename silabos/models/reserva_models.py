from odoo import models, fields, api
class reserva(models.Model):
    _name = 'silabos.reserva'
    _description="Esta Clase almacena las Reservas de la Mecanica"

    name= fields.Char('Nombres y Apellidos de quien Reserva')
    id= fields.Char('ID de la reserva ')
    hora=fields.Char('Hora de la Reserva')
