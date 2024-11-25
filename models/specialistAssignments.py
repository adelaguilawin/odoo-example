from odoo import models, fields

class SpecialistAssignment(models.Model):
    _name = 'implement_specialist_assignment'
    _description = 'Tabla de asignaciones de especialistas'

    specialist_id = fields.Many2one('implement_specialist', string='Especialista', required=True)
    activity_id = fields.Many2one('implement_activity', string='Actividad', required=True)