import collections

import logging
logger = logging.getLogger('oozappa')


def _update(org, opt):
    for k, v in opt.items():
        if isinstance(v, collections.Mapping):
            r = _update(org.get(k, OozappaSetting()), v)
            org[k] = r
        else:
            org[k] = opt[k]
    return org


class OozappaSetting(dict):
    '''dict like object. accessible with dot syntax.
    >>> settings = OozappaSetting(
    ...   spam = '123',
    ...   egg = 123
    ... )
    >>> assert(settings.spam == '123')
    >>> assert(settings.egg == 123)
    >>> settings.ham = 123.0
    >>> assert(settings.ham == 123.0)
    >>> s2 = OozappaSetting(dict(spam=456))
    >>> settings.update(s2)
    >>> assert(settings.spam == 456)
    >>> assert(settings.ham == 123.0)
    '''

    def __init__(self, *args, **kwargs):
        for d in args:
            if isinstance(d, collections.Mapping):
                self.update(d)
        for key, value in kwargs.items():
            self[key] = value

    def __setattr__(self, key, value):
        if isinstance(value, collections.Mapping):
            self[key] = OozappaSetting(value)
        else:
            self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            object.__getattribute__(self, key)

    def update(self, opt):
        self = _update(self, opt)
