import pytest

from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearch


def test_instantiate():
    search = NatureInspiredSearch()

    assert search is not None
