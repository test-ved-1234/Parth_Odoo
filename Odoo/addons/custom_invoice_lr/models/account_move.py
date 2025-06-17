from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'


    x_lr_number = fields.Char(string="LR Number")
    x_lr_date = fields.Date(string="LR Date")
    x_transport = fields.Text(string="Transport")
    x_final_total_monetory = fields.Monetary(
                                string='Final Total Money', 
                                compute='_custom_compute_final_total',
                                store=True
                                ) 
    x_rounded = fields.Float(
                            string = 'Rounding',
                            compute='_custom_compute_final_total',
                            store=True
                            )
    

    @api.depends('amount_total')
    def _custom_compute_final_total(self):
        for move in self:
            move.x_rounded = -round(move.amount_total - round(move.amount_total),2)
            move.x_final_total_monetory = round(move.amount_total)