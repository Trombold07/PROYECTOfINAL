from odoo import models, fields, api
class piezas(models.Model):
    _name = 'silabos.piezas'
    _description="Esta Clase enlista las Piezas"

    pieza= fields.Char('Nombre de la Pieza')
    cantidad= fields.Integer('Cantidad disponible de la pieza ')
    preciototal=fields.Double('Precio total de las Piezas')
    preciounitario=fields.Html('Precio unitario')