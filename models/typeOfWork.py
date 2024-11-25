from odoo import models, fields

class TypeOfWork(models.Model):
    _name = 'implement_type_of_work'
    _description = 'Tabla de tipos de trabajo'

    type = fields.Char(required=True)
    name = fields.Char(required=True)