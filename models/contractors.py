from odoo import models, fields

class Contractor(models.Model):
    _name = 'implement_contractor'
    _description = 'Tabla de contratistas'

    name = fields.Char(required=True)