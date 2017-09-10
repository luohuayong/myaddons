# -*- coding: utf-8 -*-
from odoo import http

# class Car(http.Controller):
#     @http.route('/car/car/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car/car/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car.listing', {
#             'root': '/car/car',
#             'objects': http.request.env['car.car'].search([]),
#         })

#     @http.route('/car/car/objects/<model("car.car"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car.object', {
#             'object': obj
#         })