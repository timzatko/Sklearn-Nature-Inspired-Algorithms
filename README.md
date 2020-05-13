# Nature Inspired Algorithms for scikit-learn

[![CI](https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/workflows/CI/badge.svg?branch=master)](https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/actions?query=workflow:CI+branch:master)
[![PyPI version](https://badge.fury.io/py/sklearn-nature-inspired-algorithms.svg)](https://pypi.org/project/sklearn-nature-inspired-algorithms/)
[![PyPI downloads](https://img.shields.io/pypi/dm/sklearn-nature-inspired-algorithms)](https://pypi.org/project/sklearn-nature-inspired-algorithms/)
 
Nature inspired algorithms for hyper-parameter tuning in [scikit-learn](https://github.com/scikit-learn/scikit-learn). This package uses algorithms implementation from [NiaPy](https://github.com/NiaOrg/NiaPy). 

## Installation

```shell script
pip install sklearn-nature-inspired-algorithms
```

## Usage

The usage is similar to using sklearn's `GridSearchCV`.

```python
from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = { 
    'n_estimators': range(20, 100, 20), 
    'max_depth': range(2, 20, 2),
    'min_samples_split': range(2, 20, 2), 
}

clf = RandomForestClassifier(random_state=42)

nia_search = NatureInspiredSearchCV(
    clf,
    param_grid,
    algorithm='fa', # firefly algorithm
    population_size='25',
    max_n_gen=100,
    max_stagnating_gen=5,
)

nia_search.fit(X_train, y_train)
```

Jupyter notebooks with full examples are available in [here](examples/notebooks).

### Using custom nature inspired algorithm

If you do not want to use ony of the pre-defined algorithm configurations, you can use any algorithm from the  [NiaPy](https://github.com/NiaOrg/NiaPy) collection.
This will allow you to have more control of the algorithm behaviour. 
Refer to their [documentation](https://niapy.readthedocs.io/en/latest/) and [examples](https://github.com/NiaOrg/NiaPy/tree/master/examples) for the usage. 

```python
from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV

from NiaPy.algorithms.basic import GeneticAlgorithm

param_grid = { 
    'n_estimators': range(20, 100, 20), 
    'max_depth': range(2, 20, 2),
    'min_samples_split': range(2, 20, 2), 
}

algorithm = GeneticAlgorithm()
algorithm.setParameters(NP=50, Ts=5, Mr=0.25)

nia_search = NatureInspiredSearchCV(
    clf,
    param_grid,
    algorithm=algorithm,
    max_n_gen=100,
    max_stagnating_gen=5,
)

nia_search.fit(X_train, y_train)
```

## Contributing 

Detailed information on the contribution guidelines are in the [CONTRIBUTING.md](./CONTRIBUTING.md).