from odoo import models, fields, api
from datetime import date

class GSTR3BReport(models.Model):
    _name = 'gstr3b.report'
    _description = 'GSTR-3B Report'

    name = fields.Char(string="Report Name", required=True)
    date_from = fields.Date(string="Start Date", required=True)
    date_to = fields.Date(string="End Date", required=True)

    total_taxable = fields.Monetary(string="Total Taxable Value")
    total_igst = fields.Monetary(string="IGST")
    total_cgst = fields.Monetary(string="CGST")
    total_sgst = fields.Monetary(string="SGST")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    # @api.onchange('date_from', 'date_to')
    # def compute_summary(self):
    #     invoices = self.env['account.move'].search([
    #         ('move_type', '=', 'out_invoice'),
    #         ('state', '=', 'posted'),
    #         ('invoice_date', '>=', self.date_from),
    #         ('invoice_date', '<=', self.date_to),
    #     ])
    #     igst, cgst, sgst, taxable = 0, 0, 0, 0

    #     for inv in invoices:
    #         for line in inv.invoice_line_ids:
    #             taxable += line.price_subtotal
    #             for tax in line.tax_ids:
    #                 if 'IGST' in tax.name:
    #                     igst += tax.amount * line.price_subtotal / 100
    #                 elif 'CGST' in tax.name:
    #                     cgst += tax.amount * line.price_subtotal / 100
    #                 elif 'SGST' in tax.name:
    #                     sgst += tax.amount * line.price_subtotal / 100

    #     self.total_taxable = taxable
    #     self.total_igst = igst
    #     self.total_cgst = cgst
    #     self.total_sgst = sgst
