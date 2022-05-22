import unittest

from .model_selection import NatureInspiredSearchTestCase, \
    ParamGridTestCase, \
    CrossValidationTestCase


def get_suite():
    suite = unittest.TestSuite()

    suite.addTest(NatureInspiredSearchTestCase())
    suite.addTest(ParamGridTestCase())
    suite.addTest(CrossValidationTestCase())

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
