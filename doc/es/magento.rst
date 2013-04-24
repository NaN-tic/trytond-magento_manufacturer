#:after:magento/magento:section:exportar_estado#

.. inheritref:: magento/magento:section:fabricante_magento

==================
Fabricante Magento
==================

Podemos importar los fabricantes de Magento de Magento a Tryton.

.. note:: Por defecto, el atributo de Magento que hace referencia a fabricante
          se llama **manufactuer**. Si usted le ha cambiado el nombre, deberá
          poner el nuevo nombre en la sección **Magento APP** de Tryton.

.. inheritref:: magento/magento:section:importacion_de_fabricantes

Importación de fabricantes
==========================

Para importar fabricantes de Magento a Tryton abra el menú |menu_magento_app| y
haga clic en el botón **Importar fabricantes de Magento**.

.. |menu_magento_app| tryref:: magento.menu_magento_app_form/complete_name

.. note:: Durante la importación, Tryton busca entre sus terceros aquél cuyo
          nombre coincida con el nombre del fabricante de Magento, y además
          tenga la opción **Fabricante** marcada. En el caso de encontrarlo, 
          no lo creará por lo que para que haya una relación entre los
          fabricantes de Tryton y de Magento, es importante que los nombres de
          ambos coincidan.

.. inheritref:: magento/magento:section:exportacion_de_fabricantes

Exportación fabricantes
=======================

Magento no permite la importación de fabricantes por lo que, para añadir más
fabricantes de Tryton a Magento, deberá crear los fabricantes manualmente en
Magento e importarlos posteriormente a Tryton tal y como se describe en el
apartado anterior.
