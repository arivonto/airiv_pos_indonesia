# Indonesia POS Retail & F&B Engine (Dynamic QRIS, Thermal Receipts, WhatsApp Invoicing)

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Target: QRIS & Thermal](https://img.shields.io/badge/Payment-Dynamic%20QRIS%20%26%20Thermal%20ESC%2FPOS-pink.svg)](https://airiv.id)

A modern, high-speed Indonesian Point of Sale (POS) retail and F&B engine built specifically for **Odoo 18.0 Community Edition**. Provides dynamic QRIS on-screen display, Indonesian ESC/POS 58mm/80mm thermal receipts with PPN 12% breakdown, and instant WhatsApp digital receipt delivery.

---

## Detailed Capabilities

### 1. Dynamic QRIS On-Screen Display
* **Real-Time Payment**: Generates transaction-specific dynamic QR codes on customer-facing screens or tablets.
* **Multi-E-Wallet Acceptance**: Supports BCA Mobile, Mandiri Livin', GoPay, OVO, ShopeePay, and Dana via standard ASPI EMVCo QRIS specifications.

### 2. Indonesian Thermal Receipt Engine (58mm & 80mm)
* **ESC/POS Optimization**: Pre-formatted thermal layouts for mobile EDC printers (58mm) and desktop POS counter printers (80mm).
* **Statutory PPN 12% Breakdown**: Cleanly calculates and displays DPP and PPN 12% under UU HPP regulations.
* **Coretax Ready**: Automatically prints store NPWP 16/NIK on receipt headers.

### 3. WhatsApp Digital Receipt Delivery
* **Paperless Invoicing**: Send complete itemized digital receipts directly to customer WhatsApp numbers in 1 click.
* **Integrated Auditing**: Logs delivery payloads inside Odoo with zero third-party middleware.

---

## Validated Commercial Benchmark (Tested & Scrutinized)

The complete POS workflow was verified under live Odoo 18.0 Community conditions:

1. **POS Configuration**: Main Store register configured with 80mm thermal receipt width, PPN 12% tax summary, and Dynamic QRIS payment rails.
2. **Order Execution**: POS Order `POS/2026/00001` processed for 2 items totaling **Rp 112.000,00** (DPP: Rp 100.000, PPN 12%: Rp 12.000).
3. **WhatsApp Struk Dispatch**: Dispatched itemized digital receipt to customer `0812-3456-7890`, verified in the audit logger.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL POS client compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `point_of_sale`, `account`, `base` |
| **Server Overhead** | Zero (Native ORM, direct browser QR rendering) |
