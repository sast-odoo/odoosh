# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime
from datetime import timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    expiration = fields.Datetime(string="Expiration")

# the auto-update cron job to run at midnight every day
    def _cancel_expired_orders(self):
        for record in self:
            if self.expiration: #if expiration is set; otherwise ignore
                if datetime.now().day > self.expiration.day: #if this day is past the expiration day
                    pass
