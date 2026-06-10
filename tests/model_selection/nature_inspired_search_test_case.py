import unittest

from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification


class NatureInspiredSearchTestCase(unittest.TestCase):
    def test_instantiate(self):
        search_clf = NatureInspiredSearchCV(None, {})

        self.assertIsNotNone(search_clf)

    def test_random_state_is_none(self):
        has_different = False
        prev_best_params = None

        for _ in range(0, 10):
            search_clf = self.get_classification_nature_inspired_search(search_clf_random_state=None)
            best_params = search_clf.best_params_

            if prev_best_params is not None \
                    and (prev_best_params['max_depth'] != best_params['max_depth']
                         or prev_best_params['min_samples_split'] != best_params['min_samples_split']):
                has_different = True
                break

            prev_best_params = best_params

        self.assertTrue(has_different)

    def test_random_state_is_42(self):
        has_different = False
        prev_best_params = None

        for _ in range(0, 5):
            search_clf = self.get_classification_nature_inspired_search(search_clf_random_state=42)
            best_params = search_clf.best_params_

            if prev_best_params is not None \
                    and (prev_best_params['max_depth'] != best_params['max_depth']
                         or prev_best_params['min_samples_split'] != best_params['min_samples_split']):
                has_different = True
                break

            prev_best_params = best_params

        self.assertFalse(has_different)

    def test_dict_like_parameters(self):
        # regression test for #24, dict values are not hashable,
        # so they cannot be used in the score cache key directly
        param_grid = {
            'class_weight': [{False: 1, True: 2}, {False: 1, True: 1}],
            'max_depth': range(2, 5),
        }

        X, y = make_classification(n_samples=100, n_features=20, flip_y=0.5, random_state=42)

        clf = DecisionTreeClassifier(random_state=42)
        search_clf = NatureInspiredSearchCV(clf, param_grid, algorithm='hba', max_n_gen=5, population_size=10, runs=2,
                                            random_state=42)
        search_clf.fit(X, y)

        self.assertIn(search_clf.best_params_['class_weight'], param_grid['class_weight'])

    @staticmethod
    def get_classification_nature_inspired_search(search_clf_random_state=None):
        param_grid = {
            'max_depth': range(2, 20),
            'min_samples_split': range(2, 20),
        }

        X, y = make_classification(n_samples=100, n_features=20, flip_y=0.5, random_state=42)

        clf = DecisionTreeClassifier(random_state=42)
        search_clf = NatureInspiredSearchCV(clf, param_grid, algorithm='hba', max_n_gen=5, population_size=20, runs=5,
                                            random_state=search_clf_random_state)
        search_clf.fit(X, y)

        return search_clf


if __name__ == '__main__':
    unittest.main()
