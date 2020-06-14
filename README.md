# Nature Inspired Algorithms for scikit-learn

[![CI](https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/workflows/CI/badge.svg?branch=master)](https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/actions?query=workflow:CI+branch:master)
[![Maintainability](https://api.codeclimate.com/v1/badges/ed99e5c765bf5c95d716/maintainability)](https://codeclimate.com/github/timzatko/Sklearn-Nature-Inspired-Algorithms/maintainability)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sklearn-nature-inspired-algorithms)
[![PyPI version](https://badge.fury.io/py/sklearn-nature-inspired-algorithms.svg)](https://pypi.org/project/sklearn-nature-inspired-algorithms/)
[![PyPI downloads](https://img.shields.io/pypi/dm/sklearn-nature-inspired-algorithms)](https://pypi.org/project/sklearn-nature-inspired-algorithms/)
 
Nature inspired algorithms for hyper-parameter tuning of [scikit-learn](https://github.com/scikit-learn/scikit-learn) models. This package uses algorithms implementation from [NiaPy](https://github.com/NiaOrg/NiaPy). 

## Installation

```shell script
pip install sklearn-nature-inspired-algorithms
```

## Usage

The usage is similar to using sklearn's `GridSearchCV`. Refer to the [documentation](https://sklearn-nature-inspired-algorithms.readthedocs.io/en/stable/) for more detailed guides and more examples.

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
    random_state=None, # or any number if you want same results on each run
)

nia_search.fit(X_train, y_train)

# the best params are stored in nia_search.best_params_
# finally you can train your model with best params from nia search
new_clf = RandomForestClassifier(**nia_search.best_params_, random_state=42)
```

Also you plot the search process with _line plot_ or _violin plot_.

```python
from sklearn_nature_inspired_algorithms.helpers import score_by_generation_lineplot, score_by_generation_violinplot

# line plot will plot all of the runs, you can specify the metric to be plotted ('min', 'max', 'median', 'mean')
score_by_generation_lineplot(nia_search, metric='max')

# in violin plot you need to specify the run to be plotted
score_by_generation_violinplot(nia_search, run=0)
```

Jupyter notebooks with full examples are available in [here](examples/notebooks).

### Using a Custom Nature-Inspired Algorithm

If you do not want to use any of the pre-defined algorithm configurations, you can use any algorithm from the  [NiaPy](https://github.com/NiaOrg/NiaPy) collection.
This will allow you to have more control of the algorithm behavior. 
Refer to their [documentation](https://niapy.readthedocs.io/en/latest/) and [examples](https://github.com/NiaOrg/NiaPy/tree/master/examples) for the usage. 

__Note:__ Use version >2.x.x of NiaPy package

```python
from NiaPy.algorithms.basic import GeneticAlgorithm

algorithm = GeneticAlgorithm() # when custom algorithm is provided random_state is ignored
algorithm.setParameters(NP=50, Ts=5, Mr=0.25)

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

Detailed information on the contribution guidelines are in the [CONTRIBUTING.md](./CONTRIBUTING.md).