# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Asignatura(models.Model):
    _name = 'silabos.asignatura'
    _description="Esta Clase almacena las asignaturas"

    @api.model
    @api.onchange('numero_horas')
    def mostrar_creditos(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            creditos2 = (rec.numero_horas / 16)
            rec['creditos'] = creditos2


    state= fields.Selection([
        ('verificado', 'Verificado'),
        ('modificar', 'Modificar'),
    ], "Estado", readonly=True)
    name = fields.Char('Nombre de la Asignatura')
    idAsignatura= fields.Char('Codigo de la Asignatura')
    numero_horas= fields.Integer('Numero de Horas de la Asignatura')
    creditos= fields.Integer('Numero de Creditos de la Asignatura')
    descripcion=fields.Html('Descripcion de la Asignatura')
    objetivos_especificos=fields.Html('Detalle de los Objetivos Especificos de la Asignatura')
    compeGenerica=fields.Html('Competencias Genéricas de la Asignatura')
    compeEspecifica = fields.Html('Competencias Especificas de la Asignatura')
    #horasclasePeriodo = fields.Integer('Horas de Clase por El Periodo')

    profesor_ids = fields.Many2many("silabos.profesor")
    requisito_ids = fields.One2many('silabos.requisito', 'asignatura_id', string="Requisitos")
    unidad_ids = fields.One2many('silabos.unidad', 'asignatura_id', string="Unidades")
    resultado_ids = fields.One2many('silabos.resultado', 'asignatura_id', string="Resultados de Aprendizaje de la Asignatura")
    ciclo_id = fields.Many2one('silabos.ciclo', 'Ciclos de la Asignatura')

    @api.multi
    def set_to_Verificado(self):
        """
        este metodo va a permitir leer la informaion
        """
        self.write({'state': 'verificado'})

    def set_to_modificar(self):
        """
        este metodo va a permitir modificar la asignatura
        """
        self.write({'state': 'modificar'})
