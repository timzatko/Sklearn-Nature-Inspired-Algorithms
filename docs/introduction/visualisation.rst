Visualization of Optimization Results
=====================================

If you would like to plot the optimization process, you can use one of the following built-in functions from the `sklearn_nature_inspired_algorithms.helpers` package.

score_by_generation_lineplot
----------------------------

`sklearn_nature_inspired_algorithms.helpers.score_by_generation_lineplot` plots the score (*min*, *max*, *mean*, or *median*) of each algorithm run by generation using a line plot.
The score, or "fitness" in nature-inspired algorithms, is set by the provided estimator. Estimators have a score method that provides a default evaluation criterion for the problem they are designed to solve (`reference <https://scikit-learn.org/stable/modules/model_evaluation.html#metrics-and-scoring-quantifying-the-quality-of-predictions>`_).
You can set your own score by providing the scoring parameter to :doc:`NatureInspiredSearchCV </introduction/nature-inspired-search-cv>`.

.. code-block:: python
    
    score_by_generation_lineplot(nia_search, metric='max', ax=None, ylim=None)

Parameters
~~~~~~~~~~

- **nia_search**: *NatureInspiredSearchCV object*
- **metric**: *str, default='max'*. The metric to plot. Possible values are *min*, *max*, *mean*, and *median*.
- **ax**: *matplotlib Axes*, default=None. The axes object to plot on. If not provided, one will be created.
- **ylim**: *tuple*, default=None. Only applicable if the *ax* parameter is `None`. Sets the boundaries of the *Y* axis.

Returns
~~~~~~~~~~

- **ax**: *matplotlib Axes*

Returns the Axes object with the plot drawn on it.


score_by_generation_violinplot
------------------------------

`sklearn_nature_inspired_algorithms.helpers.score_by_generation_violinplot` plots the score of a selected run by generation using violin plots.

.. code-block:: python

    score_by_generation_violinplot(nia_search, run=0, ax=None, ylim=None)

Parameters
~~~~~~~~~~

- **nia_search**: *NatureInspiredSearchCV object*
- **run**: *int, default=0*. The run to plot.
- **ax**: *matplotlib Axes*, default=None. The axes object to plot on. If not provided, one will be created.
- **ylim**: *tuple*, default=None. Only applicable if the *ax* parameter is `None`. Sets the boundaries of the *Y* axis.

Returns
~~~~~~~~~~

- **ax**: *matplotlib Axes*

Returns the Axes object with the plot drawn on it.
