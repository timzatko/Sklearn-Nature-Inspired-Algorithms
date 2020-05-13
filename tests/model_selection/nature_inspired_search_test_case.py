import unittest

from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV


class NatureInspiredSearchTestCase(unittest.TestCase):
    def test_instantiate(self):
        self.search = NatureInspiredSearchCV(None, {})

        self.assertIsNotNone(self.search)


if __name__ == '__main__':
    unittest.main()
