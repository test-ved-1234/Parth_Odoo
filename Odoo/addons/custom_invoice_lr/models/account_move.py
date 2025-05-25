from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    lr_number = fields.Char(string="LR Number")
