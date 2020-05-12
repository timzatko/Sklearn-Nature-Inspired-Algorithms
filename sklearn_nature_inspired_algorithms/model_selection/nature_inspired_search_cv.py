import numpy as np

from ._param_grid import ParamGrid
from ._parameter_search_benchmark import ParameterSearchBenchmark
from ._stagnation_stopping_task import StagnationStoppingTask

from NiaPy.algorithms.basic import FireflyAlgorithm

from sklearn.model_selection._search import BaseSearchCV


class NatureInspiredSearchCV(BaseSearchCV):
    __param_grid = None

    def _run_search(self, evaluate_candidates):
        benchmark = ParameterSearchBenchmark(evaluate_candidates, self.__param_grid)

        task = StagnationStoppingTask(
            length=len(self.__param_grid),
            n_gen=self.__n_gen,
            max_stagnating_gen=self.__max_stagnating_gen,
            benchmark=benchmark
        )

        algorithm = FireflyAlgorithm()
        algorithm.run(task=task)

    def __init__(self, estimator, param_grid, max_n_gen=100, max_stagnating_gen=5, scoring=None, n_jobs=None, iid='deprecated', refit=True, cv=None, verbose=0,
                 pre_dispatch='2*n_jobs', error_score=np.nan, return_train_score=True):
        super().__init__(estimator, scoring, n_jobs, iid, refit, cv, verbose, pre_dispatch, error_score,
                         return_train_score)

        self.__n_gen = max_n_gen
        self.__max_stagnating_gen = max_stagnating_gen
        self.__param_grid = ParamGrid(param_grid)
