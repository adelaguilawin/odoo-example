# -*- coding: utf-8 -*-
# from odoo import http


# class Implement(http.Controller):
#     @http.route('/implement/implement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/implement/implement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('implement.listing', {
#             'root': '/implement/implement',
#             'objects': http.request.env['implement.implement'].search([]),
#         })

#     @http.route('/implement/implement/objects/<model("implement.implement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('implement.object', {
#             'object': obj
#         })

