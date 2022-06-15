# -*- coding: utf-8 -*-

from odoo import models, fields, api #usually you will want to import these 3

class Spaceship(models.Model):
    _name = "spaceship" #most important field
    _description = "Spaceship Metrics"
    
    passengers = fields.integer(string="Number of Passengers", required=True)
    
    name = fields.Char(string="Name", required=True)
    
    launch = fields.date(string="Launch Date")
    
    length = fields.integer(string="Length of Ship (feet)",required=True)
    width = fields.integer(string="Width of Ship (feet)", required=True)
    height = fields.integer(string="Height of Ship (feet)", required=True)
    
    description = fields.Text(string="Description")
    
    fuel = fields.Selection(string="Fuel Type",
                             selection=[("petroleum","Petroleum"),
                                       ("cryogenic","Cryogenic"),
                                        ("hypergolic","Hypergolic")]
                           )
    
    active = fields.Boolean(string="Active",default=True) #reserved field (has functionality programmed in already)