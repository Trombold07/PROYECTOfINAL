# -*- coding: utf-8 -*-
from odoo import models, fields, api
import  pdb
class Silabo(models.Model):
    _name = 'silabos.silabo'
    _description="Esta Clase almacena los Silabos ingresados por el Docente"


    #@api.model
    #@api.onchange('asignatura_id')
    #def mostrar_unidades (self):
     #   for rec in self:
            # para iniciar el debug
            #pdb.set_trace()
      #      unid_ids =rec.unidades_ids
       #     lista=[]

        #    for unidad in unid_ids:
         #       contenidos_ids= self.env['silabos.contenido'].search([('unidad_id','=',unidad.id)])
          #      for contenido in contenidos_ids:
           #         wiz_contenido_line={
            #            'unidad_id':contenido.unidad_id,
             #           'tema':contenido.tema,
              #          'teoricas':contenido.teoricas,
               #         'practicas':contenido.practicas,
                #        'tutorias' : contenido.tutorias,
                 #       'actPractica': contenido.actPractica,
                  #      'tautonomo' :contenido.tautonomo,
                   #     'mecanismoEva':contenido.mecanismoEva,
                    #}
                    #lista.append((0,0,wiz_contenido_line))
            #rec['contUnidad']=lista

    #@api.model
    #@api.onchange('asignatura_id')
    #def mostrar_contenidos_asignatura (self):
     #  for rec in self:
      #     cont_ids = rec.contenido_ids
       #    lista = []
        #   for contenido in cont_ids:
               #contenidos_ids= self.env['silabos.contenido'].search([('u','=',contenido.id)])
         #      resulAprend
          #     for contenido in contenido_ids:
           #        wiz_contenido_line={
            #       'tema':contenido.tema,
             #      }
              #   lista.append((0,0,wiz_contenido_line))
               #  rec['contUnidad']=lista

    #@api.model
    #@api.onchange('contenido_ids')
    @api.depends('contenido_ids')
    def mostrar_sumatoria(self):
        for rec in self:
            # para iniciar el debug
            #pdb.set_trace()
            # unid_ids =rec.unidades_ids
            conten = rec.contenido_ids
            contenteoricas = 0
            contenpracticas = 0
            contentutorias = 0
            contencampo = 0
            contenautonomo = 0
            # contenidos_ids= self.env['silabos.contenido'].search([('unidad_id','=',unidad.id)])
            for contenido in conten:
                contenteoricas = contenteoricas + (contenido.teoricas)
                contenpracticas = contenpracticas + (contenido.practicas)
                contentutorias = contentutorias + (contenido.tutorias)
                contencampo = contencampo + (contenido.actPractica)
                contenautonomo = contenautonomo + (contenido.tautonomo)
            #self.Distteoricas= 8+5
            #rec['Distteoricas'] = teoricas
            #rec.distribucion.horasPractiXDocente = practicas
            #rec['distribucion_ids.virtual'] = tutorias
            #rec['distribucion_ids.horasPractiCampoTalle'] = campo
            #rec['hrsTrabAuto'] = autonomo

    @api.model
    @api.onchange('porcenhorasTeoriXDocente')
    def mostrar_horasTeoricas(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            teorica=(rec.horasPerioAsigna*int(rec.porcenhorasTeoriXDocente))/100
            rec['horasTeoriXDocente']= teorica

    @api.model
    @api.onchange('porcenhorasPractiXDocente')
    def mostrar_horasPracticas(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            practicas = (rec.horasPerioAsigna * int(rec.porcenhorasPractiXDocente)) / 100
            rec['horasPractiXDocente'] = practicas

    @api.model
    @api.onchange('porcenhorasVirtuales')
    def mostrar_virtuales(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            virtuales = (rec.horasPerioAsigna * int(rec.porcenhorasVirtuales)) / 100
            rec['virtual'] = virtuales

    @api.model
    @api.onchange('porcenPresencial')
    def mostrar_presenciales(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            presenciales = (rec.horasPerioAsigna * int(rec.porcenPresencial)) / 100
            rec['presencial'] = presenciales

    @api.model
    @api.onchange('porcenhorasPractiCampoTalle')
    def mostrar_Campo(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            campo = (rec.horasPerioAsigna * int(rec.porcenhorasPractiCampoTalle)) / 100
            rec['horasPractiCampoTalle'] = campo

    @api.model
    @api.onchange('porcenhrsTrabAuto')
    def mostrar_Autonomo(self):
        for rec in self:
            # para iniciar el debug
            # pdb.set_trace()
            autonomo = (rec.horasPerioAsigna * int(rec.porcenhrsTrabAuto)) / 100
            rec['hrsTrabAuto'] = autonomo


    name = fields.Char('Nombre del Silabo')
    value = fields.Integer()
    state  = fields.Selection([
        ('borrador','Borrador'),
        ('en_revision','En Revision'),
        ('aprobado','Aprobado')
    ],"Estado", readonly=True, default="borrador")
    carrera_id = fields.Many2one('silabos.carrera', 'Carrera ')
    asignatura_id = fields.Many2one('silabos.asignatura', 'Asignatura')
    periodo_id=fields.Many2one('silabos.periodo', 'Periodo Academico')
    evento = fields.Selection([
        ('primer_evento', 'Primer Evento'),
        ('segundo_evento', 'Segundo Evento'),
        ('tercer_evento', 'Tercer Evento'),
    ])
    nivel = fields.Char('Nivel de la Asignatura')
    #horasPerio = fields.Integer('Horas de clase por Periodo')
    profesor_id= fields.Many2one('silabos.profesor', 'Profesor de la Asignatura')
    unidad_organizacion_curricular = fields.Selection([
        ('basica', 'Basica'),
        ('profesional', 'Profesional'),
        ('titulacion', 'Titulacion'),
    ], string="Unidad Organizacional Curricular")
    #codAsignatura = fields.Char('Codigo de la Asignatura')
    ciclo_id=fields.Many2one('silabos.ciclo', 'Ciclos')
    modalidad = fields.Selection([
        ('presencial', 'Presencial'),
        ('distancia', 'Distancia'),
    ],string="Modalidad")

    creditosAsig= fields.Integer(string='Numero de Creditos')
    fecha=fields.Date(string='Fecha de Elaboracion')
    asignatura_id = fields.Many2one('silabos.asignatura','Asignatura')
    profesor_id= fields.Many2one('silabos.profesor','Docente')
    criterio_ids = fields.One2many('silabos.criterio', 'silabo_id')



    #distribucion de Horas
    horasTeoriXDocente = fields.Integer('Numero de Horas')
    porcenhorasTeoriXDocente = fields.Selection([
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
    ], string="Porcentaje")
    horasPractiXDocente = fields.Integer('Numero de Hora')

    porcenhorasPractiXDocente = fields.Selection([
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
    ], string="Porcentaje")

    virtual = fields.Integer('Numero de Horas')
    porcenhorasVirtuales = fields.Selection([
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
    ], string="Porcentaje")

    presencial = fields.Integer( 'Numero de Horas ')
    porcenPresencial = fields.Selection([
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
    ], string="Porcentaje")

    horasPractiCampoTalle = fields.Integer("Numero de Horas")
    porcenhorasPractiCampoTalle = fields.Selection([
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
    ], string="Porcentaje")

    hrsTrabAuto = fields.Integer("Numero de Horas")
    porcenhrsTrabAuto = fields.Selection([
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
    ], string="Porcentaje")



    actaEntrega_id = fields.Many2one('silabos.acta', 'Redactar Acta de Entrega del Silabo')
    #distribucion_ids = fields.One2many('silabos.distribucion', 'silabo_id')
    #requisito_ids = fields.One2many('silabos.requisito', 'silabo_id')
    unidad_ids= fields.One2many('silabos.unidad', 'silabo_id')

    relacionca_ids = fields.One2many('silabos.relacionca', 'silabo_id')
    relacionar_ids = fields.One2many('silabos.relacionar', 'silabo_id')
    semana_ids = fields.One2many('silabos.semana', 'silabo_id')
    contenido_ids = fields.One2many('silabos.contenido', 'silabo_id')
    planificacion_ids = fields.One2many('silabos.planificacion', 'silabo_id')

    #contUnidad = fields.One2many('silabos.contenido', 'silabo_id')

    bibliografia_ids = fields.One2many('silabos.bibliografia', 'silabo_id')

    # para q me aparezca el contenido  de la unidad
    # contUnidad=fields.One2many(related='unidades_ids.contenido_ids')

    semanaUnidad = fields.One2many(related='unidades_ids.semana_ids')

    # para q me aparezca la unidad de la asignatura
    unidades_ids = fields.One2many(related='asignatura_id.unidad_ids')

    #para q me aparezca el codigo de asignatura
    codAsignatura= fields.Char('Codigo de la asignatura',related= 'asignatura_id.idAsignatura' , readonly=True)
    descAsignatura = fields.Html("Descripcion de la Asignatura", related='asignatura_id.descripcion', readonly=True)
    objespeAsignatura=fields.Html("Objetivos Especificos de la Asignatura", related='asignatura_id.objetivos_especificos', readonly=True)
    compGeneAsigna=fields.Html("Competencias Genéricas de la Asignatura", related='asignatura_id.compeGenerica', readonly=True)
    compEspeAsigna=fields.Html("Competencias Especificas de la Asignatura", related='asignatura_id.compeEspecifica', readonly=True)
    credAsigna = fields.Integer("Numero de Creditos", related='asignatura_id.creditos', readonly=True)
    horasPerioAsigna= fields.Integer("Horas de Clase por Periodo", related='asignatura_id.numero_horas', readonly=True)
    reqAsigna = fields.One2many(related='asignatura_id.requisito_ids', readonly=True)
    resAsigna = fields.One2many(related='asignatura_id.resultado_ids', readonly=True)



    emaDoc = fields.Char('Email del Docente', related= 'profesor_id.email')
    titulDoc = fields.Char("TITULO(S)", related='profesor_id.titulo', readonly=True)
    especialidadDoc=fields.Char("ESPECIALIDAD/MENCIÓN", related='profesor_id.especialidad', readonly=True)
    nivelDoc = fields.Char("NIVEL", related='profesor_id.nivel', readonly=True)
    regSeneDoc=fields.Char("REGISTRO EN LA SENESCYT", related='profesor_id.registro_Senecyt', readonly=True)
    habiDoce=fields.Html("12.1. HABILIDADES QUE POSEE EL DOCENTE", related='profesor_id.habilidades', readonly=True)
    actDoce = fields.Html("12.2. ACTITUDES DEL DOCENTE", related='profesor_id.actitudesDocente', readonly=True)

    #Distteoricas = fields.Integer(related='distribucion_ids.horasTeoriXDocente', readonly=True)


    @api.multi
    def set_to_borrador(self):
         """
         este metodo va a permitir cambiar el estado
         """
         self.write({'state':'borrador'})


    @api.multi
    def set_to_revision(self):
        """
        este metodo va a permitir cambiar el estado
        """
        self.write({'state': 'en_revision'})


    @api.multi
    def set_to_aprobado(self):
        """
        este metodo va a permitir cambiar el estado
        """
        self.write({'state': 'aprobado'})

   # @api.onchnage('asignatura_id')
    #def onchange_codigoAsignatura (self):
     #   asigna_id=self.asignatura_id
      #  if asigna_id:
       #     self.codAsignatura= asigna_id.idAsignatura

    # @api.model
    #@api.onchange('')
