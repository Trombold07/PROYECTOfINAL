# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import except_orm
from odoo.exceptions import ValidationError
import  pdb
class Usuario(models.Model):
    _name = 'silabos.usuario'

    _description="Informacion de los Usuarios del sistema"


    @api.model
    def create(self,vals):
        """
         Este metodo esta rediseñado para agregar el usuario con nombre de usuario y contraseña
        """
        if vals.get('pid', _('New')) == _('New'):
            vals['pid']= self.env['ir.sequence'].next_by_code('silabos.usuario') or _('New')
        if vals.get('pid', False):
            vals['login']  = vals['pid']
            vals['password'] = vals['pid']
        else:
            raise except_orm(_("Error"),_(''' PID NO VALIDO PARA GUARDAR EN EL REGISTRO'''))
        if vals.get('cmp_id', False):
            company_vals={
                'company_ids': [(4, vals.get("cmp_id"))],
                'company_id': vals.get('cmp_id')
            }
            vals.update(company_vals)
        res = super (Usuario, self).create(vals)
        #para iniciar el debug
        #pdb.set_trace()
        emp_gpr=self.env.ref('base.group_user')


        if res.tipo_usuario=='administrador':
            grupo= self.env.ref("silabos.group_silabos_admin")
            new_grp_list=[grupo.id, emp_gpr.id]
            res.user_id.write({'groups_id' : [(6,0, new_grp_list)]})
            return res;

        if res.tipo_usuario == 'mecanico':
            grupo = self.env.ref("silabos.group_silabos_mecanico")
            new_grp_list = [grupo.id, emp_gpr.id]
            res.user_id.write({'groups_id': [(6, 0, new_grp_list)]})
            return res;
        if res.tipo_usuario == 'cliente':
            grupo = self.env.ref("silabos.group_silabos_cliente")
            new_grp_list = [grupo.id, emp_gpr.id]
            res.user_id.write({'groups_id': [(6, 0, new_grp_list)]})
            return res;




    user_id= fields.Many2one ('res.users','User ID', ondelete="cascade", required=True,  delegate=True)
    usuario_name= fields.Char(string= 'Nombres', related='user_id.name', required=True)
    usuario_id= fields.Many2one('silabos.usuario', 'Name')
    tipo_usuario= fields.Selection([
        ('admin', 'Administrador'),
        ('mecanico', 'Mecanico'),
        ('cliente','Cliente'),

    ], string='Seleccione el tipo de usuario', required=True, default="cliente", track_visibility="onchange"
    )
    imagen= fields.Binary()
    apellidos= fields.Char(string="Apellidos")
    pid= fields.Char("Id Usuario", required=True, default=lambda self: _('New'), help='ingresar el numero de cedula' )
    fecha_nacimiento = fields.Date('Fecha de Nacimeinto ')
    telefono_convencional = fields.Char('Telefono  convencional')
    telefono_celular = fields.Char('Telefono  celular')
    cedula = fields.Char(string='Cedula', size=10, required=True)

    _sql_constraints =[
        ('cedula', 'unique(cedula)',"El usuario ya fue registrado con este numero de cedula" )
    ]



