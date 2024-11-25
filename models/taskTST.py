from odoo import models, fields

class TaskTST(models.Model):
    _name = 'implement_task_tst'
    _description = 'Tabla de tareas de TST'

    contractor_id = fields.Many2one('implement_contractor', string='Contractor')
    start_time = fields.Char(required=True)
    time_duration = fields.Integer(required=True)
    require_cut = fields.Boolean()
    status_tst_id = fields.Many2one('implement_status_tst', string='Status TST')
    comment = fields.Text()