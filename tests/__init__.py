import unittest

from .helpers import PlotsTestCase
from .model_selection import NatureInspiredSearchTestCase, \
    ParamGridTestCase, \
    CrossValidationTestCase, \
    StagnationStoppingTaskTestCase


def get_suite():
    suite = unittest.TestSuite()

    suite.addTest(NatureInspiredSearchTestCase())
    suite.addTest(ParamGridTestCase())
    suite.addTest(CrossValidationTestCase())
    suite.addTest(StagnationStoppingTaskTestCase())
    suite.addTest(PlotsTestCase())

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
