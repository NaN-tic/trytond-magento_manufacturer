#This file is part magento_manufacturer module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

from magento import *
import logging

class MagentoApp(ModelSQL, ModelView):
    _name = 'magento.app'
    _description = __doc__

    manufacturer_name = fields.Char('Manufacturer',
        help='Manufacturer attribute name')

    def __init__(self):
        super(MagentoApp, self).__init__()
        self._error_messages.update({
            'manufacturer_error': 'Not exist manufacturer attribute!',
        })
        self._buttons.update({
                'core_manufacturer': {},
                })

    @ModelView.button
    def core_manufacturer(self, ids):
        """Import Manufacturers from Magento to Tryton
        Get if this manufacturer exists by name
        :return True
        """
        party_obj = Pool().get('party.party')
        manufacturer_obj = Pool().get('magento.manufacturer')

        for app in self.browse(ids):
            with ProductAttribute(app.uri,app.username,app.password) as  product_attribute_api:
                manufacturer = app.manufacturer_name or 'manufacturer'
                try:
                    attribute_options = product_attribute_api.options(manufacturer)
                except:
                    self.raise_user_error('connection_successfully')

                for option in attribute_options:
                    partner = False

                    #check if this manufacturer attribute exists in magento.manufacturer
                    manufacturers = manufacturer_obj.search([
                                            ('magento_app','=', app.id),
                                            ('value','=', option['value']),
                                            ])
                    if len(manufacturers)>0:
                        logging.getLogger('magento').info(
                            'Skip! Manufacturer %s is already exists Magento APP %s.' %
                            (option['label'],  app.name)
                            )
                        continue

                    #search manufacturer in party or create new party
                    partners = party_obj.search([
                                            ('name','=',option['label']),
                                            ('manufacturer','=', True),
                                            ])
                    if len(partners)>0:
                        partner = partners[0]
                    else:
                        if option.get('value',False):
                            vals = {
                                'name': option['label'],
                                'manufacturer': True,
                            }
                            partner = party_obj.create(vals)
                        else:
                            continue

                    #create new manufacturer
                    if partner:
                        vals = {
                            'magento_app': app.id,
                            'manufacturer': partner,
                            'value': option['value'],
                            'label': option['label'],
                        }
                        manufacturer_obj.create(vals)
                        logging.getLogger('magento').info(
                            'Manufacturer %s. Party %s.' %
                            (option['label'], partner)
                            )

        return True

MagentoApp()


class MagentoManufacturer(ModelSQL, ModelView):
    'Magento Manufacturer'
    _name = 'magento.manufacturer'
    _description = __doc__

    magento_app = fields.Many2One('magento.app','Magento App', required=True)
    manufacturer = fields.Many2One('party.party', 'Manufacturer', required=True, 
        ondelete='CASCADE')
    value = fields.Char('ID', required=True)
    label = fields.Char('Label', required=True)

MagentoManufacturer()
