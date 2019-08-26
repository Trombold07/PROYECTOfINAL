# -*- coding: utf-8 -*-
{
    'name': "Sistema de Mecanica Automatizado",

    'summary': """
        Sistema desarrollado por Xavier Gutierrez  en el ambito de Proyecto Final
        """,

    'description': """
        Sistema que permite tener una automatizacion de las mecanicas locales y nacionales
    """,

    'author': "Xavier Alexander Gutierrez Perez",
    'website': "http://www.institutolosandes.edu.ec",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sistema de Mecanica',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/silabos_silabos_security.xml',
        'security/ir.model.access.csv',
        'views/cliente_view.xml',
        'views/mecanico_view.xml',
        'views/admin_view.xml',
        'views/reserva_view.xml',
        'views/taller_view.xml',
        'views/vehiculo_view.xml',
        'views/mantenimiento_view.xml',
        'views/inventario_view.xml',
        'views/mecanica_view.xml',
        'views/proveedor_view.xml',
        'views/usuario_view.xml',
        'views/main_menu_view.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'autoinstall': False,
}