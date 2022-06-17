# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Session(models.Model):
    _name = "academy.session"
    _description = "Session Info"

    #IF we want to be able to access this model we have to add it to security csv.

    course_id = fields.Many2one(comodel_name="academy.course",
                                string="Course",
                                ondelete="cascade", #if the course id in the course model is deleted, this field will also be deleted
                                required=True) #for every session, there must be an associated course id.

    name = fields.Char(string="Title",related="course_id.name") #will look at course_id and will retreive its name

    #now that we created a many2one on the session, we have to create a one2many on a course to link back.


    #new many2one field to define an instructor
    #many2one fields are named (name)_id by convention.
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor")
    #res partner is a pre-made model meant to represent a physical or legal entity. It can be a company, an individual or even a contact address.
    # (see: https://www.odoo.com/documentation/15.0/developer/howtos/rdtraining/08_relations.html)
    #we are using it to represent the instructor.

    #student id will be many2many because each student may be in multiple sessions and each session has multiple students.
    #many2many is named (name)_ids by convention
    student_ids = fields.Many2many(comodel_name="res.partner", string="Students")
    
    #we have to create views in a new file (session_views.xml in /views) for these fields so they are visible in the ui

    start_date = fields.Date(string="Start Data",
                            default=fields.Date.today)
    duration = fields.Integer(string="Session Days",
                            default=1)
    end_date = fields.Date(string="End Date",
                            compute="_compute_end_date",
                            inverse="_inverse_end_date", #if someone wants to set the end date instead of setting the duration
                            stored=True)


    @api.depends("start_date","duration") #everytime start_date or duration changes, this will run to update the end date
    def _compute_end_date(self):
        for record in self:
            if not(record.start_date and record.duration): #check if these two are set (we will not be able to compute the end date if they are not)
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
    
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date: #if these are both set
                record.duration = (record.end_date - record.start_date).days + 1 #convert it to an int
            else:
                continue