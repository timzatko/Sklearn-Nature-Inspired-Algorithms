Class NatureInspiredSearchCV
============================

`sklearn_nature_inspired_algorithms.model_selection.NatureInspiredSearchCV` 

This class is used for hyper-parameter optimization. Its usage is similar to scikit-learn's `GridSearchCV <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_.
The optimization algorithm performs several runs. In each run, it optimizes a population of a given size for a configured number of generations.
Parameter combinations are cached, so additional optimization runs can be beneficial.

.. code-block:: python
    
    class NatureInspiredSearchCV(estimator, param_grid, algorithm='hba', population_size=50, max_n_gen=100, runs=3,
                 max_stagnating_gen=20, random_state=None, scoring=None, refit=True, verbose=0,
                 pre_dispatch='2*n_jobs', error_score=np.nan, return_train_score=True)


Parameters
~~~~~~~~~~

- **estimator**: *sklearn estimator object.* The estimator to optimize.
- **param_grid**: *dict.* Same as for `GridSearchCV`.
- **algorithm**: *str or NiaPy algorithm object, default='hba'.* The algorithm used for optimization. See :doc:`List of Supported Algorithms </introduction/algorithms>` for possible values.
- **population_size**: *int, default=50.* The number of trained estimators in the population. Smaller populations make the search faster, but the best result may not be found because the search can get stuck in a `local optimum <https://en.wikipedia.org/wiki/Local_optimum>`_ quickly. Larger populations slow down the search and can make it as slow as grid search when the population size is close to the number of parameter combinations.
- **max_n_gen**: *int, default=100.* The maximum number of generations to optimize. This value determines when the search stops. If it is too low, the search may not start converging to the optimal solution. Very high values can significantly prolong the search. If you set `max_stagnating_gen` to a reasonable value, the maximum `max_n_gen` should rarely be reached.
- **runs**: *int, default=3.* The number of independent optimization runs. Lower values speed up the search, while higher values slow it down. Optimization results for individuals (parameter combinations) are cached between runs, so each additional run should be faster than the previous one. As a result, training time does not grow linearly with the number of runs.
- **max_stagnating_gen**: *int, default=20.* If the score remains unchanged for this number of generations, optimization stops for that run. Lower values stop the search faster, while higher values prolong it. Higher values can also help prevent the search from getting stuck in local optima. If the value is too high, the algorithm may stop because it reaches `max_n_gen`.
- **random_state**: *int, default=None.* Seed for random number generation. Set this to a constant for reproducible results.
- **verbose**: *int, default=0.* Logging level. Possible values are 0, 1, and 2.
- **n_jobs**: *int, default=None.* Number of jobs to run in parallel. `None` means 1 unless used in a joblib ``parallel_backend`` context. `-1` means using all processors. This affects the number of jobs used when evaluating a model for one _individual_ (one individual may require multiple model evaluations because of cross-validation), not the whole population. Current nature-inspired algorithm implementations do not support multiprocessing across the whole population. Multiprocessing is useful only when you use cross-validation.

.. note::
    Parallelization is process-based. scikit-learn handles it via `joblib <https://joblib.readthedocs.io/>`_ and its default ``loky`` backend.
    In environments where spawning processes is not possible (e.g. when Python is embedded in another application, such as a .NET host via pythonnet), it may fail with errors like ``OSError: [Errno 22] Invalid argument``.
    In such environments, either leave ``n_jobs=None`` or use joblib's threading backend, which avoids spawning processes:

    .. code-block:: python

        from joblib import parallel_backend

        with parallel_backend('threading'):
            search.fit(X, y)

The following parameters are inherited from scikit-learn's `BaseSearchCV <https://github.com/scikit-learn/scikit-learn/blob/1045d16ec13b1cab7878e7555538573d1884aad3/sklearn/model_selection/_search.py#L410>`_ and behave the same way as they do in `GridSearchCV`: **scoring**, **refit**, **verbose**, **pre_dispatch**, **error_score**, and **return_train_score**.
Refer to the `GridSearchCV documentation <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_ for details.

When using multi-metric **scoring** (e.g. ``scoring={'AUC': 'roc_auc', 'F1': 'f1_macro'}``), the **refit** parameter must be set to the name of the metric to optimize (e.g. ``refit='F1'``).
Unlike exhaustive search in `GridSearchCV`, the nature-inspired algorithm needs a single objective to optimize, so ``refit=False`` is not supported with multi-metric scoring.


Glossary
--------

    - An *individual* is a parameter combination trained during the optimization run. Results for each individual are *cached* between runs.
    - A *population* is a group of individuals in one generation, or step, of the optimization.

Attributes
~~~~~~~~~~

- **optimization_logs_**: *dict.* Logs from optimization runs containing the scores (fitness) of every individual in the population for each generation.
