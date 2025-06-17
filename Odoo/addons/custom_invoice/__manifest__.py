{
    'name': 'Custom GSTR-3B',
    'category': 'Accounting/Accounting',
    'version': '1.0',
    'summary': 'Generate and export GSTR-3B from Odoo',
    'author' : 'Vaidik Patel',
    'depends': ['account'],
    'data': [
        'views/gstr3b_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
