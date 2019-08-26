# -*- coding: utf-8 -*-
from odoo import models, fields, api
class acta(models.Model):
    _name = 'silabos.cliente'
    _description="Esta Clase almacena los Clientes de la Mecanica"

    name= fields.Char('Nombres y Apellidos del Cliente')
    cedula= fields.Char('Cedula del Cliente ')
    direccion=fields.Char('Direccion del Cliente')
    telefono= fields.Char('Telefono del Cliente ')





