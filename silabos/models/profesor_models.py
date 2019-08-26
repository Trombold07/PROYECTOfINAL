# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Profesor(models.Model):
    _name = 'silabos.profesor'
    _description="Esta Clase almacena el perfil de los profesores del ITSLA"

    name = fields.Char('Nombre del Profesor')
    imagen = fields.Binary()

    titulo = fields.Char('Titulo del Profesor')
    especialidad = fields.Char('Especialidad del Profesor')
    nivel = fields.Char('Nivel del Profesor')
    registro_Senecyt= fields.Char('Codigo de Registro Senecyt')
    cedula = fields.Char('Cedula del Profesor')
    email = fields.Char('Email del Profesor')
    senecyt = fields.Char('Codigo de Registro Senecyt')
    habilidades= fields.Html('Habilidades que posee el docente')
    actitudesDocente = fields.Html('Actitudes del Docente')