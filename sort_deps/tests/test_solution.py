from solution import sort_deps


def test_sort_deps():
    assert sort_deps({
        'mongo': [],
        'tzinfo': ['thread_safe'],
        'uglifier': ['execjs'],
        'execjs': ['thread_safe', 'json'],
        'redis': [],
    }) == [
        'mongo',
        'thread_safe',
        'tzinfo',
        'json',
        'execjs',
        'uglifier',
        'redis',
    ]

    assert sort_deps({
        'right': ['predicated', 'sexp_processor'],
        'poetry': ['requests'],
        'predicated': ['htmlentities'],
        'sexp_processor': [],
        'requests': ['right'],
        'virtuses': [],
    }) == [
        'htmlentities',
        'predicated',
        'sexp_processor',
        'right',
        'requests',
        'poetry',
        'virtuses',
    ]

    assert sort_deps({
        'wrong': ['django', 'processor'],
        'xpath': ['nokogiri'],
        'django': ['uwsgi'],
        'processor': [],
        'nokogiri': ['wrong', 'libxml2'],
        'libxml2': ['libxslt'],
        'virtus': [],
    }) == [
        'uwsgi',
        'django',
        'processor',
        'wrong',
        'libxslt',
        'libxml2',
        'nokogiri',
        'xpath',
        'virtus',
    ]
