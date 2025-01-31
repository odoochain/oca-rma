import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-rma",
    description="Meta package for oca-rma Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_warranty>=15.0dev,<15.1dev',
        'odoo-addon-rma>=15.0dev,<15.1dev',
        'odoo-addon-rma_delivery>=15.0dev,<15.1dev',
        'odoo-addon-rma_sale>=15.0dev,<15.1dev',
        'odoo-addon-rma_sale_mrp>=15.0dev,<15.1dev',
        'odoo-addon-stock_production_lot_warranty>=15.0dev,<15.1dev',
        'odoo-addon-website_rma>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
