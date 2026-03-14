{
   'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real Estate Management System',
    'description': """
        Manage properties, owners, and sales.
    """,
    'author': 'Nahom Biniam',
    'category': 'Real Estate',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'view/estate_property_views.xml',
       
    ],
    'installable': True,
    'application': True,

}
