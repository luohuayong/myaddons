# -*- coding: utf-8 -*-
from odoo import http



class CrudTest(http.Controller):
    @http.route('/crud_test/1', auth='public')
    def test1(self):
        result = ''
        openacademy_course = http.request.env['openacademy.course']
        result += openacademy_course.search([]).__str__() + '<br/>'
        result += openacademy_course.search([], limit=1).name.__str__() + '<br/>'
        # result += openacademy_course.create({'name': "new_course1"}).__str__() + '<br/>'
        result += openacademy_course.browse([1]).name.__str__() + '<br/>'
        result += openacademy_course.search_count([]).__str__() + '<br/>'
        # result += openacademy_course.search([('name', '=', 'new_course1')])\
        #               .write({'name': 'new_course11'}).__str__() + '<br/>'
        # result += openacademy_course.search([('name', '=', 'new_course11')]).unlink().__str__() + '<br/>'
        # result += openacademy_course.search([]).__str__() + '<br/>'
        return result

# class CrudTest(http.Controller):
#     @http.route('/crud_test/crud_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crud_test/crud_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crud_test.listing', {
#             'root': '/crud_test/crud_test',
#             'objects': http.request.env['crud_test.crud_test'].search([]),
#         })

#     @http.route('/crud_test/crud_test/objects/<model("crud_test.crud_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crud_test.object', {
#             'object': obj
#         })