from odoo import models, fields

class Activity(models.Model):
    _name = 'implement_activity'
    _description = 'Tabla de actividades'

    date = fields.Date(required=True)
    time_start = fields.Char(required=True)
    time_end = fields.Char(required=True)
    type = fields.Char(required=True)
    location = fields.Char(required=True)
    specialist_id = fields.Many2one('implement_specialist', string='Specialist')