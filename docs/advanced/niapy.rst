Using a Custom NiaPy Algorithm
==============================

If you do not want to use one of the predefined algorithm configurations, you can use any algorithm from the `NiaPy <https://github.com/NiaOrg/NiaPy>`_ collection.
This gives you more control over the algorithm behavior.
Refer to the NiaPy `documentation <https://niapy.readthedocs.io/en/latest/>`_ and `examples <https://github.com/NiaOrg/NiaPy/tree/master/examples>`_ for usage details.

.. note::
    Use NiaPy version 2.7.0 or later.

.. code-block:: bash

    pip install 'niapy>=2.7.0'

Example
-------

Usage is almost the same as with a predefined algorithm. Instead of passing a shorthand value, pass the NiaPy algorithm object via the ``algorithm`` parameter.

.. code-block:: python

    from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from niapy.algorithms.basic import GeneticAlgorithm

    param_grid = { 
        'n_estimators': range(20, 100, 20), 
        'max_depth': range(2, 40, 2),
        'min_samples_split': range(2, 20, 2), 
        'max_features': ["auto", "sqrt", "log2"],
    }

    clf = RandomForestClassifier(random_state=42)

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

    # The best parameters are stored in:
    # nia_search.best_params_
