{
    'name': 'Library Extensions',
    'version': '1.0',
    'summary': 'Extensions for the library module',
    'depends': ['library'],  # This assumes your base module is called 'library'
    'data': [
        'views/library_book_views.xml',
        'views/library_book_category_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}