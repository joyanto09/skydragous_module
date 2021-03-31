{
    'name': 'Internal Transfer Partenr Name',
    'summary': 'Generate To Internal Transfer Partner',
    'author': 'Metamorphosis',
    'license': 'AGPL-3',
    'website': 'http://odoo.metamorphosis.com.bd/',
    'category': 'Accounting',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'account',
    ],
    'data': [
        'views/account_payment_view.xml',
    ],
    'installable': True,
    'application': True,
}