from odoo import models, fields

class StatusTST(models.Model):
    _name = 'implement_status_tst'
    _description = 'Tabla de estados de TST'

    name = fields.Char(required=True)