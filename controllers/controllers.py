# -*- coding: utf-8 -*-
# from odoo import http


# class SkHacking(http.Controller):
#     @http.route('/sk_hacking/sk_hacking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sk_hacking/sk_hacking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sk_hacking.listing', {
#             'root': '/sk_hacking/sk_hacking',
#             'objects': http.request.env['sk_hacking.sk_hacking'].search([]),
#         })

#     @http.route('/sk_hacking/sk_hacking/objects/<model("sk_hacking.sk_hacking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sk_hacking.object', {
#             'object': obj
#         })
