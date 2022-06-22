# -*- coding: utf-8 -*-

{
    "name" : "TVU",

    "summary" : """TVU module to auto-delete expired orders""",

    "description":"""
        TVU Module to add functionality for auto-deleting expired orders at midnight every night
    """,

    "author":"Sam Struble",

    "version":"0.1",

    "depends" : ["sale"],

    "data" : [
        "views/sale_views_inherit.xml",
        "data/sale_order_data.xml"
    ],

    "demo" : []

}
