Basic Usage
===========

This page covers the basics of using the library.

Installation
------------

Install the library with **pip** package manager.

.. code-block:: bash

   pip install sklearn-nature-inspired-algorithms


Usage
-----

The usage is similar to using sklearn's `GridSearchCV <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_.
In the following example, we assume that you are already familiar with the basics of the scikit-learn library. Also you need to have it installed.

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
      random_state=None, # or any number if you want same results on each run
   )

   nia_search.fit(X_train, y_train)

After you have fit the `NatureInspiredSearchCV`, you can retrieve the best parameters in the same way as with `GridSearchCV` using the `best_params_` property. 
You can use them to train the final model.

.. code-block:: python
   new_clf = RandomForestClassifier(**nia_search.best_params_, random_state=42)

If you would like to plot the optimization process you can use one of the built-in functions described in :doc:`Visualisation of Optimization Results </introduction/visualisation>`.

.. note::
   The fitness of each invididual in the optimization process is defined by the score method of your estimator or the scoring parameter provided to the :doc:`NatureInspiredSearchCV </introduction/nature-inspired-search-cv>`.

Examples
--------

Jupyter Notebooks with examples are available `here <https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms/tree/master/examples/notebooks>`_.
