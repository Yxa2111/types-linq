from typing import TypedDict


class ModuleSpec(TypedDict):
    file_path: str
    name: str
    classes: dict[str, 'ClassSpec']

class ClassSpec(TypedDict):
    methods: set[str]
    readonly_properties: set[str]

# ==========================================================
# This describes which APIs are exported for doc

_path = '../types_linq'

_project = 'types_linq'

type_file = f'{_path}/more_typing.py'

modules: list[ModuleSpec] = [
    {
        'file_path': f'{_path}/cached_enumerable.py',
        'name': f'{_project}.cached_enumerable',
        'classes': {
            'CachedEnumerable': {
                'methods': {
                    'as_cached',
                },
                'readonly_properties': {*()},
            },
        },
    },
    {
        'file_path': f'{_path}/enumerable.pyi',
        'name': f'{_project}.enumerable',
        'classes': {
            'Enumerable': {
                'methods': {
                    '__init__',
                    '__contains__',
                    '__getitem__',
                    '__iter__',
                    '__len__',
                    '__reversed__',
                    'aggregate',
                    'all',
                    'any',
                    'append',
                    'as_cached',
                    'average',
                    'average2',
                    'cast',
                    'concat',
                    'contains',
                    'count',
                    'default_if_empty',
                    'distinct',
                    'element_at',
                    'empty',
                    'except1',
                    'first',
                    'first2',
                    'group_by',
                    'group_by2',
                    'group_join',
                    'intersect',
                    'join',
                    'last',
                    'last2',
                    'max',
                    'max2',
                    'min',
                    'min2',
                    'of_type',
                    'order_by',
                    'order_by_descending',
                    'prepend',
                    'range',
                    'repeat',
                    'reverse',
                    'select',
                    'select2',
                    'select_many',
                    'select_many2',
                    'sequence_equal',
                    'single',
                    'single2',
                    'skip',
                    'skip_last',
                    'skip_while',
                    'skip_while2',
                    'sum',
                    'sum2',
                    'take',
                    'take_last',
                    'take_while',
                    'take_while2',
                    'to_dict',
                    'to_set',
                    'to_list',
                    'to_lookup',
                    'union',
                    'where',
                    'where2',
                    'zip',
                    'zip2',
                    'elements_in',
                    'to_tuple',
                },
                'readonly_properties': {*()},
            },
        },
    },
    {
        'file_path': f'{_path}/grouping.py',
        'name': f'{_project}.grouping',
        'classes': {
            'Grouping': {
                'methods': {*()},
                'readonly_properties': {
                    'key',
                },
            },
        },
    },
    {
        'file_path': f'{_path}/lookup.py',
        'name': f'{_project}.lookup',
        'classes': {
            'Lookup': {
                'methods': {
                    '__contains__',
                    '__len__',
                    '__getitem__',
                    'apply_result_selector',
                    'contains',
                },
                'readonly_properties': {
                    'count',
                },
            },
        },
    },
    {
        'file_path': f'{_path}/ordered_enumerable.pyi',
        'name': f'{_project}.ordered_enumerable',
        'classes': {
            'OrderedEnumerable': {
                'methods': {
                    'create_ordered_enumerable',
                    'then_by',
                    'then_by_descending',
                },
                'readonly_properties': {*()},
            }
        },
    },
    {
        'file_path': f'{_path}/types_linq_error.py',
        'name': f'{_project}.types_linq_error',
        'classes': {
            'TypesLinqError': {
                'methods': {*()},
                'readonly_properties': {*()},
            },
            'InvalidOperationError': {
                'methods': {*()},
                'readonly_properties': {*()},
            },
            'IndexOutOfRangeError': {
                'methods': {*()},
                'readonly_properties': {*()},
            },
        },
    },
]
