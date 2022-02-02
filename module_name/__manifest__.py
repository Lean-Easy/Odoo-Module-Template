# -*- coding: utf-8 -*-
{
    'name': 'MODULE_NAME',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': 'SHORT_DESCRIPTION',
    'author': "AUTHOR",
    'website': "WEBSITE",
    'depends': ['base'],
    'data': [
        # Uncomment below if needed
        # 'security/ir.model.access.csv',
        # 'views/module_name_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            # for css, scss, js in static/src/...
		],
		'web.assets_qweb': [
            # for xml in static/src/...
		]
    }
}
