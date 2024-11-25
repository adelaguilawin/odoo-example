# -*- coding: utf-8 -*-
{
    'name': "implement",
    'summary': "Modulo de Plataforma implementacion",
    'description': """
Long description of module's purpose
    """,
    'author': "Jack",
    'website': "https://www.winempresas.pe",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

