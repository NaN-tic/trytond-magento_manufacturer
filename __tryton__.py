#This file is part magento_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Magento Manufacturer',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Magento Manufacturer''',
    'depends': [
        'ir',
        'res',
        'product_manufacturer',
    ],
    'xml': [
        'magento_core.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
