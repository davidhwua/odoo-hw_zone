# -*- coding: utf-8 -*-
{
    'name': "hw_zone",

    'summary': """
        海文省份、城市模块""",

    'description': """
       海文省份、城市模块
    """,

    'author': "Emmet Duan",
    'website': "http://www.harmonywin.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail',
                'base',
                'web',
                    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hw_zone.xml',
        'views/menuitem.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [

    ],

    'application':True,
    'installable':True,
    'auto_install': False, 
}