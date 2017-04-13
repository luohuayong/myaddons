# -*- coding: utf-8 -*-
from odoo import http

# class Qingjia(http.Controller):
#     @http.route('/qingjia/qingjia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qingjia/qingjia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qingjia.listing', {
#             'root': '/qingjia/qingjia',
#             'objects': http.request.env['qingjia.qingjia'].search([]),
#         })

#     @http.route('/qingjia/qingjia/objects/<model("qingjia.qingjia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qingjia.object', {
#             'object': obj
#         })