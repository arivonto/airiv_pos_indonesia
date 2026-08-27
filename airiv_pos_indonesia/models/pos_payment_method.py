# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    l10n_id_payment_type = fields.Selection([
        ('cash', 'Tunai (Cash IDR)'),
        ('qris_dynamic', 'Dynamic QRIS (Midtrans / Xendit Core API)'),
        ('qris_static', 'Static QRIS (ASPI / Merchant QRIS Code)'),
        ('transfer', 'Bank Transfer (BCA / Mandiri / BRI / BNI)'),
        ('edc', 'Mesin EDC Debit / Kartu Kredit'),
    ], string="Indonesian Payment Rail", default='cash')

    l10n_id_qris_merchant_id = fields.Char(string="QRIS Merchant ID (NMID)")
    l10n_id_qris_static_payload = fields.Text(string="Static QRIS Code String / URL", help="Raw EMVCo / ASPI QRIS payload string")
