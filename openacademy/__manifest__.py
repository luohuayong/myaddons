# -*- coding: utf-8 -*-
{
    'name': "开放学院",

    'summary': """
        开放学院培训管理模型：
        课程、授课、听课人注册""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Leo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/templates.xml',
        'demo/demo.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
