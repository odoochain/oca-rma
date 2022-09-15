# Part of PLSuite Professional. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

{
    'name': 'Paddle Law RMAs',
    'version': '15.0.1.0.1',
    'category': 'Warehouse',
    'author': 'PaddleLaw Corp.',
    'license': 'OPL-1',
    'website': 'https://paddle.law/',
    'depends': [
        'pl_base',
        'stock',
        'delivery',
    ],
    'demo': [
        'demo/rma_demo.xml',
    ],
    'data': [
        'data/cron_data.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'security/rma_security.xml',
        'views/account_views.xml',
        'views/portal_templates.xml',
        'views/rma_views.xml',
        'views/stock_picking_views.xml',
        'wizard/rma_lines_views.xml',
        'wizard/rma_make_rtv_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
 }
