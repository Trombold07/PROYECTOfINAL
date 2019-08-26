# -*- coding: utf-8 -*-
from odoo import http

# class Silabos(http.Controller):
#     @http.route('/silabos/silabos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/silabos/silabos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('silabos.listing', {
#             'root': '/silabos/silabos',
#             'objects': http.request.env['silabos.silabos'].search([]),
#         })

#     @http.route('/silabos/silabos/objects/<model("silabos.silabos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('silabos.object', {
#             'object': obj
#         })