# -*- coding: utf-8 -*-
from odoo import http

# class QwebTest(http.Controller):
#     @http.route('/qweb_test/qweb_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qweb_test/qweb_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qweb_test.listing', {
#             'root': '/qweb_test/qweb_test',
#             'objects': http.request.env['qweb_test.qweb_test'].search([]),
#         })

#     @http.route('/qweb_test/qweb_test/objects/<model("qweb_test.qweb_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qweb_test.object', {
#             'object': obj
#         })