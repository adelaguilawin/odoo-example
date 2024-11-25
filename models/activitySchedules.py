from odoo import models, fields

class ActivitySchedule(models.Model):
    _name = 'implement_activity_schedule'
    _description = 'Tabla de programación de actividades'

    ticket_ev = fields.Char(required=True)
    type_work_id = fields.Many2one('implement_type_of_work', string='Type of Work')
    client_id = fields.Many2one('implement_client', string='Client')
    date_exec = fields.Date(required=True)
    task_pin_id = fields.Many2one('implement_task_pin', string='Task PIN')
    task_tst_id = fields.Many2one('implement_task_tst', string='Task TST')