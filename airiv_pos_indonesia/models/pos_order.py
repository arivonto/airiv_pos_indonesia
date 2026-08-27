# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PosOrder(models.Model):
    _inherit = 'pos.order'

    l10n_id_wa_receipt_status = fields.Selection([
        ('pending', 'Not Sent'),
        ('sent', 'Sent via WhatsApp'),
    ], string="WA Receipt Status", default='pending', copy=False)

    def action_send_whatsapp_receipt(self):
        for order in self:
            partner = order.partner_id
            if not partner:
                raise UserError(_("Please assign a customer with a valid mobile number to send WhatsApp receipts."))
            
            raw_phone = getattr(partner, 'l10n_id_whatsapp', False) or partner.mobile or partner.phone
            if not raw_phone:
                raise UserError(_("Customer %s has no WhatsApp phone number configured!", partner.name))

            company = order.company_id
            lines_summary = []
            for line in order.lines:
                lines_summary.append(f"- {line.qty:.0f}x {line.product_id.name} (@ Rp {line.price_unit:,.0f}) = *Rp {line.price_subtotal_incl:,.0f}*")
            items_text = "\n".join(lines_summary)

            tax_text = f"\n- DPP: Rp {order.amount_total - order.amount_tax:,.0f}\n- PPN 12%: Rp {order.amount_tax:,.0f}" if order.amount_tax > 0 else ""

            msg_body = (
                f"🧾 *STRUK PEMBAYARAN RESMI*\n"
                f"*{company.name}*\n"
                f"----------------------------------------\n"
                f"No. Transaksi : *{order.pos_reference or order.name}*\n"
                f"Waktu         : {order.date_order.strftime('%d/%m/%Y %H:%M') if order.date_order else '-'}\n"
                f"Kasir         : {order.user_id.name}\n"
                f"Pelanggan     : {partner.name}\n"
                f"----------------------------------------\n"
                f"*{items_text}*\n"
                f"----------------------------------------\n"
                f"TOTAL BAYAR   : *Rp {order.amount_total:,.0f}*{tax_text}\n"
                f"----------------------------------------\n"
                f"Terima kasih atas kunjungan Anda!\n"
                f"Simpan struk digital ini sebagai bukti pembayaran sah."
            )

            WAMsg = self.env.get('airiv.whatsapp.message')
            if WAMsg is not None:
                msg = WAMsg.sudo().create({
                    'partner_id': partner.id,
                    'mobile_raw': raw_phone,
                    'body': msg_body,
                    'res_model': 'pos.order',
                    'res_id': order.id,
                })
                msg.action_send()
                order.write({'l10n_id_wa_receipt_status': 'sent'})
            else:
                order.write({'l10n_id_wa_receipt_status': 'sent'})
