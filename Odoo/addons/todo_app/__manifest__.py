{
    'name': 'To Do Apps',
    'category': 'Services/Todo',
    'version': '1.0.1',
    'author': 'Vaidik Patel',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}