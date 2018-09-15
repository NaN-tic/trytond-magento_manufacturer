# This file is part magento_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta
from magento import *
import logging

__all__ = ['MagentoApp', 'MagentoManufacturer']

logger = logging.getLogger(__name__)


class MagentoApp(metaclass=PoolMeta):
    __name__ = 'magento.app'
    manufacturer_name = fields.Char('Manufacturer',
        help='Manufacturer attribute name')

    @classmethod
    def __setup__(cls):
        super(MagentoApp, cls).__setup__()
        cls._error_messages.update({
            'manufacturer_error': 'Not exist manufacturer attribute!',
        })
        cls._buttons.update({
                'core_manufacturer': {},
                })

    @classmethod
    @ModelView.button
    def core_manufacturer(self, apps):
        """Import Manufacturers from Magento to Tryton
        Get if this manufacturer exists by name
        :return True
        """
        Party = Pool().get('party.party')
        Manufacturer = Pool().get('magento.manufacturer')

        to_create = []
        for app in apps:
            with ProductAttribute(app.uri, app.username, app.password) as \
                    product_attribute_api:
                manufacturer = app.manufacturer_name or 'manufacturer'
                try:
                    attribute_options = product_attribute_api.options(
                        manufacturer)
                except:
                    self.raise_user_error('manufacturer_error')

                for option in attribute_options:
                    partner = None

                    #check if this manufacturer attribute exists
                    manufacturers = Manufacturer.search([
                                    ('magento_app', '=', app.id),
                                    ('value', '=', option['value']),
                                    ], limit=1)
                    if manufacturers:
                        logger.info('Skip! Manufacturer '
                            '%s is already exists Magento APP %s.' %
                            (option['label'], app.name))
                        continue

                    #search manufacturer in party or create new party
                    partners = Party.search([
                                    ('name', '=', option['label']),
                                    ('manufacturer', '=', True),
                                    ], limit=1)
                    if partners:
                        partner, = partners
                    else:
                        if option.get('value', False):
                            vals = {
                                'name': option['label'],
                                'manufacturer': True,
                            }
                            partner = Party.create([vals])[0]
                        else:
                            continue

                    #create new manufacturer
                    if partner:
                        to_create.append({
                            'magento_app': app.id,
                            'manufacturer': partner,
                            'value': option['value'],
                            'label': option['label'],
                        })
                        logger.info(
                            'Manufacturer %s. Party %s.' %
                            (option['label'], partner)
                            )
        if to_create:
            Manufacturer.create(to_create)


class MagentoManufacturer(ModelSQL, ModelView):
    'Magento Manufacturer'
    __name__ = 'magento.manufacturer'
    magento_app = fields.Many2One('magento.app', 'Magento App', required=True)
    manufacturer = fields.Many2One('party.party', 'Manufacturer',
        required=True, ondelete='CASCADE')
    value = fields.Char('ID', required=True)
    label = fields.Char('Label', required=True)
