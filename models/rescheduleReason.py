from odoo import models, fields

class RescheduleReason(models.Model):
    _name = 'implement_reschedule_reason'
    _description = 'Tabla de razones de reprogramación'

    name = fields.Char(required=True)