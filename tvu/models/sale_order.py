# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = "sale.order"

    expiration = fields.Datetime(string="Expiration")