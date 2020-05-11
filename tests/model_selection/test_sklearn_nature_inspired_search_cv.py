import pytest

from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV


def test_instantiate():
    search = NatureInspiredSearchCV(None)

    assert search is not None
