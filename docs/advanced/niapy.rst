Using a Custom NiaPy Algorithm
==============================

If you do not want to use any of the pre-defined algorithm configurations, you can use any algorithm from the `NiaPy <https://github.com/NiaOrg/NiaPy>`_ collection.
This will allow you to have more control of the algorithm behavior. 
Refer to their `documentation <https://niapy.readthedocs.io/en/latest/>`_ and `examples <https://github.com/NiaOrg/NiaPy/tree/master/examples>`_ for the usage. **Note:** Use version >2.x.x of NiaPy package.

.. code-block:: bash

    pip install NiaPy==2.0.0rc10


Example
-------

The usage is almost the same, instead of using the pre-defined algorithm, you pass the NiaPy algorithm object via algorithm parameter.

.. code-block:: python

    from sklearn_nature_inspired_algorithms.model_selection import NatureInspiredSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from NiaPy.algorithms.basic import GeneticAlgorithm

    param_grid = { 
        'n_estimators': range(20, 100, 20), 
        'max_depth': range(2, 40, 2),
        'min_samples_split': range(2, 20, 2), 
        'max_features': ["auto", "sqrt", "log2"],
    }

    clf = RandomForestClassifier(random_state=42)

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

    # The most optimal parameters are stored in:
    # nia_search.best_params_
