YACT - Yet Another Configuration Tool
=====================================
#### A JSON based Python configuration tool

Installation
------------

    pip install yact

Usage
-----

Examples:

*/etc/yact/default.json* - First file loaded

    {
        "test": {
           "more": {
                "final": {
                    "value": 123
                }
           },
           "another": "another value"
        },
        "foo": "bar"
    }

*~/.yact/default.json* - These values overwrite the above

    {
        "test": {
           "more": {
                "final": {
                    "value": 456
                }
           }
        },
        "boo": "far"
    }

*/etc/yact/test.json* - These values overwrite the above

    {
        "test": {
           "test_only": "test only param"
        },
        "foo": "foobar"
    }

Run

    YACT_ENV=test YACT__FOO="another foo" python
    >>> from yact.yact import *
    >>>
    >>> c = create_config()
    >>> print c
    {u'test': {u'test_only': u'test only param', u'another': u'another value', u'more': {u'final': {u'value': 456}}}, u'foo': u'another foo', u'boo': u'far'}
    >>> c.get('test.more.final.value')
    123
    >>> c.get('test.more.final.value.foo', 'unkown')
    'unknown'

*./development.json* - These values overwrite the above

    {
        "test": {
           "test_only": "test only param"
        },
        "foo": "foobar"
    }

Run

    python
    >>> from yact import Yact
    >>>
    >>> c = Yact(env='test', default_file='development.json', config_paths=['./'], **{'a': 'b'})
    >>> c
    { "a": "b", "test": { "test_only": "test only param"}, "foo": "foobar"}
    >>>
    >>> c == dict(c)
    True
    >>>
    >>> c == Config(**c)
    True

Run

    python
    >>> from yact import Config
    >>>
    >>> c = Config()
    >>> c
    {}
    >>> c['x'] = {'y': 'z'}
    >>> c
    {'x': {'y': 'z'}}
    >>> c.get('x.y')
    'z'
    >>> c.get('x.y.z', 'oops')
    'oops'
    >>> type(c)
    <class 'yact.Config'>
    >>> c == dict(c)
    True




Configuration
-------------

By default Yact looks for JSON formatted configuration files in the following:

* /etc/yact
* ~/.yact

These can be overridden by a comma separated string in the `YACT_CONFIG_PATHS` environment variable

    export YACT_CONFIG_PATHS=/etc/my_app/configs,/etc/my/configs

Yact will load configuration files based on the `YACT_ENV` environment variable. For example:

    export YACT_ENV=production

By default files called `default.json` located in the `YACT_CONFIG_PATHS` are loaded. If `YACT_ENV` exists, it will attempt to overlay values in `{YACT_ENV}.json` files over the `default.json` values. These files MUST be valid JSON.

The default file loaded can by changed with the `YACT_DEFAULT_FILE` environment variable.

Configuration settings can be passed in via environment variables in the following way:

    YACT__SOME__KEY_ID="some value" -> {"some": {"key_id": "some value"}}

Notice how two underscores are used to separate nested objects.

The order in which values are set for the configuration are as follows:

* Load all `default.json` files (from all `YACT_CONFIG_PATHS` in order received)
* Load all `{YACT_ENV}.json` files (from all `YACT_CONFIG_PATHS` in order received)
* Load environment variable overrides
* Override values from any passed into Class as kwargs
