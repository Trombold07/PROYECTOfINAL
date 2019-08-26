# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Bibliografia(models.Model):
    _name = 'silabos.bibliografia'
    _description="Esta Clase referencia los contenidos de la asignatura de ITSLA"

    autor = fields.Char('Nombre del Autor')
    titulo = fields.Char('Titulo del Libro')
    lugarPrublicacion = fields.Char('Ciudad, Pais de Publicacion')
    edicion = fields.Char('Edicion')
    anioPublicacion = fields.Date('Fecha de Publicacion')
    editorial = fields.Char('Editorial')
    isbn = fields.Char('ISBN/ISSN')

    nombre= fields.Selection([
        ('basica','Basica'),
        ('complementaria', 'Complementaria'),
    ],"nombre", readonly=True, default="basica")

    tipo= fields.Selection([
        ('fisica','Fisica'),
        ('virtual', 'Virtual'),
        #('recursosinternet', 'Recursos en Internet'),
    ],"tipo", readonly=True, default="fisica")

    contenido_id = fields.Many2one('silabos.contenido', 'Agregar Contenido')
    silabo_id= fields.Many2one('silabos.silabo', "Agregar Silabo")

