from odoo import models, fields

class Client(models.Model):
    _name = 'implement_client'
    _description = 'Tabla de clientes'

    address = fields.Char(required=True)
    district = fields.Char(required=True)
    contact = fields.Char(required=True)
    phone = fields.Char(required=True)