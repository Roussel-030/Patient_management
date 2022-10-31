# -*- coding: utf-8 -*-
{
    'name': "patient_management",

    'summary': """
        long description patient management""",

    'description': """
        patient management
    """,

    'author': "Kasia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',
        # views
        'views/patient_management_views.xml',
        # wizard
        'wizard/patient_popup_views.xml',
        # report
        'report/patient_management_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
