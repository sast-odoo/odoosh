# -*- coding: utf-8 -*-

from odoo import models, fields, api

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