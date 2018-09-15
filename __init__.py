# This file is part magento_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import magento_core
from . import product

def register():
    Pool.register(
        magento_core.MagentoApp,
        magento_core.MagentoManufacturer,
        product.Product,
        module='magento_manufacturer', type_='model')
