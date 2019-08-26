from odoo import models, fields, api
class proveedor(models.Model):
    _name = 'silabos.proveedor'
    _description="Esta Clase enlista los Proveedores"

    nombre= fields.Char('Nombre del Proveedor')
    telefono= fields.Char('telefono del Proveedor ')
    direccion=fields.Char('Direccion del Proveedor')
    descripcion=fields.Html('Descripcion del Proveedor')
