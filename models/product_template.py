# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template" #technical name for the thing we're inheriting from.

    is_session_product = fields.Boolean(string="Use as Session Product",
                                        help="Check this box to use this as a Product for Session Fee.",
                                        default=False)

    