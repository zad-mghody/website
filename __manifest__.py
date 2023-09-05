{
    'name': "My Website",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'sequence': 3,
    'website': "https://www.yourcompany.com",
    'category': 'website',
    'version': '0.1',
    'depends': ['base', 'auth_signup', 'web'],
    'data': [
        'views/phone_number_views.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
