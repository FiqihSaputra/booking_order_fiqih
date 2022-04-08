# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderFiqih(http.Controller):
#     @http.route('/booking_order_fiqih/booking_order_fiqih/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_fiqih/booking_order_fiqih/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_fiqih.listing', {
#             'root': '/booking_order_fiqih/booking_order_fiqih',
#             'objects': http.request.env['booking_order_fiqih.booking_order_fiqih'].search([]),
#         })

#     @http.route('/booking_order_fiqih/booking_order_fiqih/objects/<model("booking_order_fiqih.booking_order_fiqih"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_fiqih.object', {
#             'object': obj
#         })
