# This file is part magento_weight module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Product']


class Product:
    __metaclass__ = PoolMeta
    __name__ = "product.product"

    @classmethod
    def magento_import_product(cls, values, shop=None):
        MagentoManufacturer = Pool().get('magento.manufacturer')

        vals = super(Product, cls).magento_import_product(values, shop)

        manufacturer = values.get('manufacturer')
        if manufacturer:
            manufacturers = MagentoManufacturer.search([
                ('value','=', manufacturer),
                ], limit=1)
        
            if manufacturers:
                mgn_manufacturer, = manufacturers
                vals['manufacturer'] = mgn_manufacturer.manufacturer
        return vals

    @classmethod
    def magento_export_product(cls, app, product, shop=None, lang='en_US'):
        MagentoManufacturer = Pool().get('magento.manufacturer')

        vals = super(Product, cls).magento_export_product(app, product, shop, lang)

        if product.manufacturer:
            manus = MagentoManufacturer.search([
                ('manufacturer', '=', product.manufacturer),
                ], limit=1)
            if manus:
                vals['manufacturer'] = manus[0].value
        return vals
