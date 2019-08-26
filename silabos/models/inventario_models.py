from odoo import models, fields, api
class inventario(models.Model):
    _name = 'silabos.inventario'
    _description="Esta Clase enlista el inventario"

    pieza= fields.Char('Nombre de la Pieza')
    cantidad= fields.Integer('Cantidad disponible de la pieza ')
    preciototal=fields.Integer('Precio total de las Piezas')
    preciounitario=fields.Integer('Precio unitario')
    descripcionpiezas= fields.Html('Descripcion de la pie')