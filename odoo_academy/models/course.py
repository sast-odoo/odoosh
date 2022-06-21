# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char(string="Title",required=True)
    description = fields.Text(string="Description")

    level = fields.Selection(string="Level",
                            selection= [    ("beginner","Beginner"),
                                            ("intermediate","Intermediate"),
                                            ("advanced","Advanced")],
                            copy=False)
    
    active = fields.Boolean(string="Active",default=True)


    base_price = fields.Float(string="Base Price", default=0.00)
    additional_fee = fields.Float(string="Additional Fee",default=10.00)
    total_price = fields.Float(string="Total Price",readonly=True)

    #ONE2MANY FIELD TO LINK TO SESSIONS
    session_ids = fields.One2many(comodel_name="academy.session",
                                    inverse_name="course_id", #name of the field of the session id
                                    string="Sessions")

    # IF THE BASE PRICE/ADDITIONAL FEE PRICE CHANGES, RE-CALCULATE THE TOTAL PRICE
    @api.onchange("base_price","additional_fee") #Trigger whenever base price or additional fee change
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError("Base Price cannot be set as negative you cheapo!")

        self.total_price = self.base_price + self.additional_fee

    #We want to make sure the additional fee is always greater than $10.
    @api.constrains("additional_fee") #Set a CONSTRAINT on additional fee to check additional fee.
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError("Additional fees cannot be less than $10.00: %s" % record.additional_fee)