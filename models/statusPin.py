from odoo import models, fields

class StatusPin(models.Model):
    _name = 'implement_status_pin'
    _description = 'Tabla de estados de PIN'

    name = fields.Char(required=True)