{
    'name': 'Meta Purchase Approval',  
    'summary': 'Approval For Purchase Order',
    'author': 'Metakave Software Solutions',
    'license': 'AGPL-3',
    'website': 'https://metakave.com/',
    'category': 'Purchase',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'purchase','web', 'mail',
    ],
    'data': [
        
        'security/purchase_security.xml',
        'views/purchase_view.xml',
        # 'backend_assets.xml',
        
    ],
    'installable': True,
}