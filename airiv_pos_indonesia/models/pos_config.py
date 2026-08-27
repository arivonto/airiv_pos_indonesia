# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    l10n_id_receipt_paper_width = fields.Selection([
        ('58mm', '58 mm (Standard Mobile Thermal / EDC)'),
        ('80mm', '80 mm (Desktop Desktop Thermal Printer)'),
    ], string="Thermal Paper Width", default='80mm', help="Optimizes receipt layout padding and line wrapping for Indonesian thermal printers")

    l10n_id_show_tax_breakdown = fields.Boolean(string="Show PPN 12% Breakdown", default=True, help="Display statutory DPP and PPN 12% summary on thermal receipts")
    l10n_id_store_npwp = fields.Char(string="Store NPWP / NIK (16 Digits)", help="Displayed in thermal receipt header for DJP Coretax compliance")
    l10n_id_auto_send_wa_receipt = fields.Boolean(string="Auto-Offer WhatsApp Digital Receipt", default=True)
