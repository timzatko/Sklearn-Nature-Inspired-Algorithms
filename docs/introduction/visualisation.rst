Visualisation of Optimization Results
=====================================

If you would like to plot the optimization process you can use one of the following built-in functions from pacakge `sklearn_nature_inspired_algorithms.helpers`.

score_by_generation_lineplot
----------------------------

`sklearn_nature_inspired_algorithms.helpers.score_by_generation_lineplot` Plots the score (*min*, *max*, *mean* or *median*) of each algorithm run by generation of the optimization process using the lineplot.
The score (or "fitness" in the field of nature-inspired algorithms) is set by the provided estimator. Estimators have a score method providing a default evaluation criterion for the problem they are designed to solve (`reference <https://scikit-learn.org/stable/modules/model_evaluation.html#metrics-and-scoring-quantifying-the-quality-of-predictions>`). 
You can set your own score by providing the scoring paramter to the `NatureInspiredSearchCV </introduction/nature-inspired-search-cv>`.

.. code-block:: python
    
    score_by_generation_lineplot(nia_search, metric='max', ax=None, ylim=None)

Parameters
~~~~~~~~~~

- **nia_search**: *NatureInspiresSearchCV object*
- **metric**: *str, default='max'*. The metric to be plotted, can be *min*, *max*, *mean* or *median*.
- **ax**: *matplotlib Axes*, default=None. The axes object where to be plotted. If not defined, it will be created.
- **ylim**: *tuple*, default=None. Only applicable if the *ax* parameter is `None`, it sets the boundaries to *Y* axis.

Returns
~~~~~~~~~~

- **ax**: *matplotlib Axes*

Returns the Axes object with the plot drawn onto it.


score_by_generation_violinplot
------------------------------

`sklearn_nature_inspired_algorithms.helpers.score_by_generation_lineplot` Plots the score of some run by generation of the optimization process using the violinplots.

.. code-block:: python

    score_by_generation_violinplot(nia_search, run=0, ax=None, ylim=None)

Parameters
~~~~~~~~~~

- **nia_search**: *NatureInspiresSearchCV object*
- **run**: *int, default=0*. The run to be plotted.
- **ax**: *matplotlib Axes*, default=None. The axes object where to be plotted. If not defined, it will be created.
- **ylim**: *tuple*, default=None. Only applicable if the *ax* parameter is `None`, it sets the boundaries to *Y* axis.

Returns
~~~~~~~~~~

- **ax**: *matplotlib Axes*

Returns the Axes object with the plot drawn onto it.

