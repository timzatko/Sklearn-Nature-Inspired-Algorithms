Class NatureInspiredSearchCV
============================

`sklearn_nature_inspired_algorithms.model_selection.NatureInspiredSearchCV` 

This class is used fot hyper-parameter optimization. Its usage is similiar to the sklearn's `GridSearchCV <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_.
The optimization algorithm does several runs, in which it optimizes the population of a certain size for a certain amount of generations.
The same parameter combinations are being cached, so it can be beneficial to make more optimization runs.

.. code-block:: python
    
    class NatureInspiredSearchCV(estimator, param_grid, algorithm='hba', population_size=50, max_n_gen=100, runs=3,
                 max_stagnating_gen=20, random_state=None)


Parameters
~~~~~~~~~~

- **estimator**: *sklearn estimator object object.*
- **param_grid**: *dict.* Same as for the `GridSearchCV`.
- **algorithm**: *str or NiaPy algorithm object, default='hba'.* Algorithm which will be used for optimization, refer to the :doc:`List of Supported Algorithms </introduction/algorithms>` for possible values.
- **population_size**: *int, default=50.* Number of trained estimators in the population.
- **max_n_gen**: *int, default=100.* The maximum number of generations which can be optimized.
- **runs**: *int, default=3.* The number of independent optimization runs to be done.
- **max_stagnating_gen**: *int, default=20.* If the score remains unchaged for the number of generations defined by this parameter, the optimization will be stopped for that particular run.
- **random_state**: *int, default=None.* Seed for the random.


Attributes
~~~~~~~~~~

- **runs_**: *int.* Number of optimization runs.
- **optimization_logs_**: *dict.* Logs from optimization runs contains scores (fitness) of every individual of the population in each generation.
