# Indonesia POS Retail & F&B Engine

[![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-0f766e.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-AIRIV-0891b2.svg)](https://airiv.id)
[![GitHub Actions](https://github.com/arivonto/airiv_pos_indonesia/actions/workflows/odoo-appstore-ci.yml/badge.svg?branch=18.0)](https://github.com/arivonto/airiv_pos_indonesia/actions)
[![Apps Store Ready](https://img.shields.io/badge/Odoo%20Apps%20Store-ready-22c55e.svg)](https://apps.odoo.com/)

AIRIV POS Indonesia is an Indonesian Point of Sale localization layer for Odoo 18 Community. It adds QRIS payment rail classification, 58/80mm thermal receipt settings, PPN 12% receipt breakdown, store NPWP/NIK metadata, and WhatsApp digital receipt dispatch for retail and F&B operations.

## Core Capabilities & Architecture

### Core capabilities

- Indonesian POS payment rails: cash IDR, dynamic QRIS, static QRIS, bank transfer, and EDC card method classification.
- QRIS metadata: merchant ID and static QRIS payload fields on POS payment methods.
- Thermal receipt readiness: POS configuration for 58mm mobile thermal and 80mm counter printers.
- Statutory receipt context: store NPWP/NIK field and optional DPP/PPN 12% receipt breakdown.
- WhatsApp receipt action: itemized receipt message from paid POS orders with customer, cashier, order, tax, and total evidence.
- AIRIV ecosystem compatibility: integrates with `airiv.whatsapp.message` when the AIRIV WhatsApp module is installed and falls back to POS receipt status tracking when it is not.

### Architecture

```text
Odoo Point of Sale
  |
  |-- POS configuration
  |-- products and customers
  |-- POS orders
  |-- payment methods
  v
AIRIV POS Indonesia Layer
  |
  |-- Indonesian payment rail classification
  |-- QRIS merchant and static payload fields
  |-- 58/80mm receipt configuration
  |-- NPWP/NIK receipt metadata
  |-- PPN 12% receipt summary
  v
Receipt and Evidence Workflow
  |
  |-- itemized POS order
  |-- cashier and customer context
  |-- DPP and PPN amount
  |-- WhatsApp digital receipt status
```

## Feature & Workflow Automation

1. Configure POS counter
   - Open POS configuration and set thermal paper width, store NPWP/NIK, statutory tax breakdown, and WhatsApp receipt preference.

2. Prepare payment rails
   - Review or create Indonesian payment methods for QRIS Dynamic, Static QRIS, bank transfer, EDC card, and cash IDR.

3. Execute checkout
   - Process retail or F&B POS orders while preserving product, customer, cashier, payment, tax, and order reference evidence.

4. Send digital receipt
   - From a paid, done, or invoiced POS order, send an itemized official receipt to the customer WhatsApp number and update receipt delivery status.

## Technical Specifications

| Item | Detail |
| --- | --- |
| Odoo series | 18.0 |
| Odoo edition | Community |
| Module technical name | `airiv_pos_indonesia` |
| Version | `18.0.1.0.0` |
| License | LGPL-3 |
| Author | AIRIV |
| Category | Sales/Point of Sale |
| Dependencies | `point_of_sale`, `account`, `base` |
| Main models | `pos.config`, `pos.payment.method`, `pos.order` |
| POS configuration fields | `l10n_id_receipt_paper_width`, `l10n_id_show_tax_breakdown`, `l10n_id_store_npwp`, `l10n_id_auto_send_wa_receipt` |
| Payment method fields | `l10n_id_payment_type`, `l10n_id_qris_merchant_id`, `l10n_id_qris_static_payload` |
| POS order fields/actions | `l10n_id_wa_receipt_status`, `action_send_whatsapp_receipt` |
| Store assets | `icon.png`, `banner.png`, `index.html` |

## Installation Guidance

1. Clone the repository branch for Odoo 18:

   ```bash
   git clone -b 18.0 https://github.com/arivonto/airiv_pos_indonesia.git
   ```

2. Place the module in your Odoo addons path.

3. Restart Odoo.

4. Activate developer mode if needed.

5. Update the Apps list.

6. Search for `Indonesia POS Retail & F&B Engine`.

7. Install the module.

## Configuration Checklist

- Confirm Odoo Point of Sale and Accounting are installed.
- Configure POS counters and select 58mm or 80mm thermal receipt width.
- Fill store NPWP/NIK metadata for Indonesian receipt context.
- Enable PPN 12% breakdown where statutory receipt details are required.
- Review Indonesian payment methods: QRIS Dynamic, Static QRIS, bank transfer, EDC, and cash IDR.
- Fill QRIS merchant ID or static QRIS payload when applicable.
- Assign customer mobile or WhatsApp numbers before using digital receipt dispatch.
- If AIRIV WhatsApp integration is installed, verify its gateway configuration before production sending.

## Repository Layout

```text
airiv_pos_indonesia/
  README.md
  LICENSE
  .github/
    workflows/
      odoo-appstore-ci.yml
    scripts/
      validate_odoo_appstore.py
  airiv_pos_indonesia/
    __manifest__.py
    data/
      pos_payment_method_data.xml
    models/
      pos_config.py
      pos_order.py
      pos_payment_method.py
    security/
      ir.model.access.csv
    static/
      description/
        icon.png
        icon_128.png
        airiv_store_icon.png
        airiv_store_icon_128.png
        banner.png
        index.html
    views/
      pos_config_views.xml
      pos_menu_views.xml
      pos_order_views.xml
      pos_payment_method_views.xml
  static/
    description/
      icon.png
      icon_128.png
      airiv_store_icon.png
      airiv_store_icon_128.png
      banner.png
      index.html
```

## Contact Info

| Item | Detail |
| --- | --- |
| Author | AIRIV |
| Website | https://airiv.id |
| GitHub | https://github.com/arivonto |
| Module repository | https://github.com/arivonto/airiv_pos_indonesia |
| Odoo series | 18.0 |

## Quality Gate

This repository is prepared for Odoo Apps Store submission with:

- Parseable Odoo manifest metadata.
- Root and module-level documentation.
- Odoo Apps Store description fragment.
- Required store images.
- LGPL-3 license metadata.
- GitHub Actions Apps Store audit on branch `18.0`.

