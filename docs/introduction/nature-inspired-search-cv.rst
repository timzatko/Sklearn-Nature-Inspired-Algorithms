Class NatureInspiredSearchCV
============================

`sklearn_nature_inspired_algorithms.model_selection.NatureInspiredSearchCV` 

This class is used for hyper-parameter optimization. Its usage is similiar to the sklearn's `GridSearchCV <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_.
The optimization algorithm does several runs, in which it optimizes the population of a certain size for a certain amount of generations.
The same parameter combinations are being cached, so it can be beneficial to make more optimization runs.

.. code-block:: python
    
    class NatureInspiredSearchCV(estimator, param_grid, algorithm='hba', population_size=50, max_n_gen=100, runs=3,
                 max_stagnating_gen=20, random_state=None, scoring=None, refit=True, verbose=0,
                 pre_dispatch='2*n_jobs', error_score=np.nan, return_train_score=True)


Parameters
~~~~~~~~~~

- **estimator**: *sklearn estimator object object.*
- **param_grid**: *dict.* Same as for the `GridSearchCV`.
- **algorithm**: *str or NiaPy algorithm object, default='hba'.* Algorithm which will be used for optimization, refer to the :doc:`List of Supported Algorithms </introduction/algorithms>` for possible values.
- **population_size**: *int, default=50.* The number of trained estimators in the population. When the population size is smaller the search will run faster, however, the best result might not be found since the search might stuck in the `local optimum <https://en.wikipedia.org/wiki/Local_optimum>` quickly. Bigger values slow down the search which can lead to the search being as slow as the grid search (when the population size is equal/close to the number of parameter combinations).
- **max_n_gen**: *int, default=100.* The maximum number of generations which can be optimized. This value determines when the search will be stopped. If you set this value too low, the search might not start to converge to the optimal solution. However high values can significantly prolong the search. If you set the `max_stagnating_gen` to a reasonable value, the maximum of `max_n_gen` should never be reached.
- **runs**: *int, default=3.* The number of independent optimization runs to be done. Low values will speed up the search, high values will slow it down. The optimization results for individuals (a combination of parameters) are being cached between the runs, so every additional run should be faster than the previous one. Hence the training time does not linearly grow with the number of runs (it grows logarithmically).
- **max_stagnating_gen**: *int, default=20.* If the score remains unchanged for the number of generations defined by this parameter, the optimization will be stopped for that particular run. Lower values will stop the search faster, higher values prolong the search time. If the algorithm is stagnating for example for 20 generations the optimization time of those 20 generations is not that long, since in most of the algorithms the majority of the population will be the neighbors of the best individual and over time those neighbors will be cached. Higher values also help to prevent being stuck in the local optima. If the value is too high, the algorithm might be stopped by `max_n_gen`.
- **random_state**: *int, default=None.* Seed for the random. Set this to some constant if you want to achieve consistent results.
- **verbose**: *int, default=0.* The level of the logging, possible values: 0, 1, 2.
- **n_jobs**: *int, default=None.* Number of jobs to run in parallel. None means 1 unless in a joblib.parallel_backend context. -1 means using all processors. This affects the number of jobs when evaluating a model for one _individual_ (for one individual there might be more model evaluations because of cross-validation) not for the whole population - current implementations of nature-inspired algorithms do not support multiprocessing. You will benefit from multiprocessing only if you use cross-validation.

The following parameters: **scoring**, **refit**, **verbose**, **pre_dispatch**, **error_score**, **return_train_score**, are inherited from sklearn's `BaseSearchCV <https://github.com/scikit-learn/scikit-learn/blob/1045d16ec13b1cab7878e7555538573d1884aad3/sklearn/model_selection/_search.py#L410>`_ and are the same as for the GridSearchCV.
Refer to the GridSearchCV `documentation <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_ to find out what they do.


Glossary
--------

    - an *individual* is a parameter combination which is trained during the optimization run. The results for every invididual are *cached* between runs.
    - a *population* is a group of invididuals in one generation/step of the optimization.

Attributes
~~~~~~~~~~

- **optimization_logs_**: *dict.* Logs from optimization runs contains scores (fitness) of every individual of the population in each generation.
