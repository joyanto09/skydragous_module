{
    'name': 'Meta Sale Approval',  
    'summary': 'Approval For Sale Order',
    'author': 'Metakave Software Solutions',
    'license': 'AGPL-3',
    'website': 'https://metakave.com/',
    'category': 'Sale',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'sale', 'mail',
    ],
    'data': [
        
        'security/sale_security.xml',
        'views/sale_view.xml',
        
    ],
    'installable': True,
}