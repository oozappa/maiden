import doctest
from maiden import config


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(config))
    return tests
