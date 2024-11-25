from odoo import models, fields

class Specialist(models.Model):
    _name = 'implement_specialist'
    _description = 'Tabla de especialistas'

    name = fields.Char(required=True)
    status = fields.Char(required=True)
    email = fields.Char(required=True)
    reason = fields.Char()
    return_date = fields.Date()
    assigned_activities = fields.One2many('implement_activity', 'specialist_id', string='Assigned Activities')