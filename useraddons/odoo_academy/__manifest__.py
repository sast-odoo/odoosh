# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        
        "security/academy_security.xml", #LINK THE SECURITY XML FILE BEFORE ACCESS RIGHTS CSV
        "security/ir.model.access.csv",

        "views/academy_menuitems.xml"
        
    ],
    
    'demo': [
        
        "demo/academy_demo.xml"
        
    ]
    
}