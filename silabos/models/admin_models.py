from odoo import models, fields, api
class admin(models.Model):
    _name = 'silabos.admin'
    _description="Esta Clase almacena los Administradores del Sistema"

    name= fields.Char('Nombres y Apellidos del Administrador')
    id= fields.Char('ID del Administrador ')
    direccion=fields.Char('Direccion del Administrado')
    telefono= fields.Char('Telefono del Administrador ')
    correo = fields.Char('Correo para Contacto')

