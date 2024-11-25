from odoo import models, fields

class TaskPin(models.Model):
    _name = 'implement_task_pin'
    _description = 'Tabla de tareas de PIN'

    start_time = fields.Char(required=True)
    end_time = fields.Char(required=True)
    time_duration = fields.Integer(required=True)
    status_pin_id = fields.Many2one('implement_status_pin', string='Status PIN')
    rq_pin = fields.Char(required=True)
    reschedule_reason_id = fields.Many2one('implement_reschedule_reason', string='Reschedule Reason')
    comment = fields.Text()