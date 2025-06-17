from datetime import datetime
import pytz
from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Done')
    date_from = fields.Text(string="Created Date")
