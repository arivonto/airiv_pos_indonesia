# -*- coding: utf-8 -*-
{
    'name': 'Indonesia POS Retail & F&B Engine (Dynamic QRIS, Thermal Receipts, WhatsApp Invoicing)',
    'version': '18.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Dynamic QRIS On-Screen Display, 58/80mm Thermal Receipt Formatting, PPN 12% Breakdown, and WhatsApp Receipts',
    'description': """
Indonesia Point of Sale (POS) Localization for Odoo 18 Community.
- Dynamic QRIS Display & Payment Engine (Midtrans / Xendit / Static QRIS ASPI standards)
- Indonesian Thermal ESC/POS Receipt Formats (58mm & 80mm with PPN 12% and NPWP / Coretax metadata)
- Instant WhatsApp Digital Receipt Delivery via Fonnte & Native Offline Sandbox
- Pre-configured Indonesian Payment Methods (QRIS, Tunai IDR, Transfer BCA/Mandiri/BRI, EDC Debit)
- Zero External Server Overhead - 100% Odoo 18 Community Native
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': ['point_of_sale', 'account', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'data/pos_payment_method_data.xml',
        'views/pos_config_views.xml',
        'views/pos_payment_method_views.xml',
        'views/pos_order_views.xml',
        'views/pos_menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
