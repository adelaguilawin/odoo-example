# -*- coding: utf-8 -*-

from odoo import models, fields


class Work(models.Model):
    _name = 'implement_work'
    _description = 'Tabla de trabajos'

    name = fields.Char(required=True)
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()