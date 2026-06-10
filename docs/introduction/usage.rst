Basic Usage
===========

This page covers the basics of using the library.

Installation
------------

Install the library with the **pip** package manager.

.. code-block:: bash

   pip install sklearn-nature-inspired-algorithms


Usage
-----

Usage is similar to scikit-learn's `GridSearchCV <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_.
The following example assumes that you are already familiar with the basics of scikit-learn and have it installed.

.. code-block:: python

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

After fitting `NatureInspiredSearchCV`, you can retrieve the best parameters the same way you would with `GridSearchCV`, using the `best_params_` property.
You can use them to train the final model.

.. code-block:: python

   new_clf = RandomForestClassifier(**nia_search.best_params_, random_state=42)

If you would like to plot the optimization process, you can use one of the built-in functions described in :doc:`Visualization of Optimization Results </introduction/visualisation>`.

.. note::
   The fitness of each individual in the optimization process is defined by your estimator's score method or by the scoring parameter provided to :doc:`NatureInspiredSearchCV </introduction/nature-inspired-search-cv>`.

Examples
--------

Jupyter notebooks with examples are available in the `examples/notebooks directory <https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/tree/master/examples/notebooks>`_.
