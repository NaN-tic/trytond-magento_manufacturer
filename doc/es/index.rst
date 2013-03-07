==================
Fabricante Magento
==================

El módulo Fabricante Magento añade un botón para importar los fabricantes
(atributo **manufacturer**) de Magento a Tryton.

.. note:: Por defecto, el atributo de Magento que hace referencia a fabricante
          se llama **manufactuer**. Si usted le ha cambiado el nombre, deberá
          poner el nuevo nombre en la sección **Magento APP** de Tryton.

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

Exportación fabricantes
=======================

Magento no permite la importación de fabricantes por lo que, para añadir más
fabricantes de Tryton a Magento, deberá crear los fabricantes manualmente en
Magento e importarlos posteriormente a Tryton tal y como se describe en el
apartado anterior.

Módulos de los que depende
==========================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /esale/index
   /esale_product/index
   /magento/index
   /product_manufacturer/index

Dependencias
------------

* `Comercio electrónico`_
* `Productos de comercio electrónico`_
* Magento_
* Fabricante_

.. _Comercio electrónico: ../esale/index.html
.. _Productos de comercio electrónico: ../esale_product/index.html
.. _Magento: ../magento/index.html
.. _Fabricante: ../product_manufacturer/index.html
