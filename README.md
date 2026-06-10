# Nature-Inspired Algorithms for scikit-learn

[![CI](https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/actions/workflows/ci.yml?query=branch%3Amaster)
![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Ftimzatko%2FSklearn-Nature-Inspired-Algorithms%2Fmaster%2Fpyproject.toml)
[![PyPI version](https://badge.fury.io/py/sklearn-nature-inspired-algorithms.svg)](https://pypi.org/project/sklearn-nature-inspired-algorithms/)
[![PyPI downloads](https://img.shields.io/pypi/dm/sklearn-nature-inspired-algorithms)](https://pypi.org/project/sklearn-nature-inspired-algorithms/)
[![Fedora package](https://img.shields.io/fedora/v/python3-sklearn-nature-inspired-algorithms?color=blue&label=Fedora%20Linux&logo=fedora)](https://src.fedoraproject.org/rpms/python-sklearn-nature-inspired-algorithms)

Nature-inspired algorithms for hyper-parameter tuning of [scikit-learn](https://github.com/scikit-learn/scikit-learn) models. This package uses algorithm implementations from [NiaPy](https://github.com/NiaOrg/NiaPy).

## Installation

```shell script
$ pip install sklearn-nature-inspired-algorithms
```

To install this package on Fedora, run:

```sh
$ dnf install python3-sklearn-nature-inspired-algorithms
```

## Usage

Usage is similar to scikit-learn's `GridSearchCV`. Refer to the [documentation](https://sklearn-nature-inspired-algorithms.readthedocs.io/en/stable/) for detailed guides and examples.

```python
from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = { 
    'n_estimators': range(20, 100, 20), 
    'max_depth': range(2, 40, 2),
    'min_samples_split': range(2, 20, 2), 
    'max_features': ["auto", "sqrt", "log2"],
}

clf = RandomForestClassifier(random_state=42)

nia_search = NatureInspiredSearchCV(
    clf,
    param_grid,
    algorithm='hba', # hybrid bat algorithm
    population_size=50,
    max_n_gen=100,
    max_stagnating_gen=10,
    runs=3,
    random_state=None, # or any number for reproducible results
)

nia_search.fit(X_train, y_train)

# The best parameters are stored in nia_search.best_params_.
# You can use them to train the final model.
new_clf = RandomForestClassifier(**nia_search.best_params_, random_state=42)
```

You can also plot the search process with a _line plot_ or a _violin plot_.

```python
from sklearn_nature_inspired_algorithms.helpers import score_by_generation_lineplot, score_by_generation_violinplot

# The line plot shows all runs. You can choose the metric to plot: 'min', 'max', 'median', or 'mean'.
score_by_generation_lineplot(nia_search, metric='max')

# For the violin plot, specify the run to plot.
score_by_generation_violinplot(nia_search, run=0)
```

Jupyter notebooks with full examples are available in [examples/notebooks](examples/notebooks).

### Using a Custom Nature-Inspired Algorithm

If you do not want to use one of the predefined algorithm configurations, you can use any algorithm from the [NiaPy](https://github.com/NiaOrg/NiaPy) collection.
This gives you more control over the algorithm behavior.
Refer to the NiaPy [documentation](https://niapy.readthedocs.io/en/latest/) and [examples](https://github.com/NiaOrg/NiaPy/tree/master/examples) for usage details.

__Note:__ Use NiaPy version 2.5.1 or later.

```python
from niapy.algorithms.basic import GeneticAlgorithm

algorithm = GeneticAlgorithm() # When a custom algorithm is provided, random_state is ignored.
algorithm.set_parameters(NP=50, Ts=5, Mr=0.25)

nia_search = NatureInspiredSearchCV(
    clf,
    param_grid,
    algorithm=algorithm,
    population_size=50,
    max_n_gen=100,
    max_stagnating_gen=20,
    runs=3,
)

nia_search.fit(X_train, y_train)
```

## Contributing 

Detailed contribution guidelines are available in [CONTRIBUTING.md](./CONTRIBUTING.md).
