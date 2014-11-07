# This file is part magento_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from .magento_core import *


def register():
    Pool.register(
        MagentoApp,
        MagentoManufacturer,
        module='magento_manufacturer', type_='model')
