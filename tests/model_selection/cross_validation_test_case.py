from unittest.mock import Mock
from unittest import TestCase, main

from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV

from sklearn.datasets import make_classification
from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GroupKFold


class MockClassifierProxy(BaseEstimator):
    # scikit creates a clone of the estimator, to preserve calls on our mock we will make it static
    Mock = Mock()

    def __init__(self, **kwargs):
        self.estimator = DecisionTreeClassifier(**kwargs)

    def fit(self, *args, **kwargs):
        self.Mock.fit(*args, **kwargs)
        return self.estimator.fit(*args, **kwargs)

    def predict(self, *args, **kwargs):
        self.Mock.predict(*args, **kwargs)
        return self.estimator.predict(*args, **kwargs)

    def score(self, **params):
        self.Mock.score(**params)
        return self.estimator.score(**params)

    def get_params(self, deep=True):
        self.Mock.get_params(deep=deep)
        return self.estimator.get_params(deep=deep)

    def set_params(self, **params):
        self.Mock.set_params(**params)
        return self.estimator.set_params(**params)


class CrossValidationTestCase(TestCase):
    def setUp(self):
        self.estimator = MockClassifierProxy()

    def test_cv_is_int(self):
        nia_search = self._get_nia_search(self.estimator, cv=3)

        X, y = make_classification(n_samples=100, n_features=20, flip_y=0.5, random_state=42)
        nia_search.fit(X, y)

        # set_params should be called each time new instance of estimator is created - for each individual in population
        method_calls = self.estimator.Mock.set_params.call_count
        self.assertEqual(25 * 3 + 1, method_calls)

    def test_cv_is_object(self):
        nia_search = self._get_nia_search(self.estimator, cv=GroupKFold(n_splits=3))

        X, y = make_classification(n_samples=1000, n_features=20, n_classes=5, n_informative=10, flip_y=0.5,
                                   random_state=42)
        nia_search.fit(X, y, groups=y)

        # set_params should be called each time new instance of estimator is created - for each individual in population
        method_calls = self.estimator.Mock.set_params.call_count
        self.assertEqual(152, method_calls)

    @staticmethod
    def _get_nia_search(clf, cv):
        param_grid = {
            'max_depth': [2, 3, 4, 5, 6],
            'min_samples_split': [2, 3, 4, 5, 6],
        }

        return NatureInspiredSearchCV(
            clf,
            param_grid,
            cv=cv,
            algorithm='hba',
            max_n_gen=5,
            population_size=20,
            runs=5,
            random_state=42,
        )


if __name__ == '__main__':
    main()
