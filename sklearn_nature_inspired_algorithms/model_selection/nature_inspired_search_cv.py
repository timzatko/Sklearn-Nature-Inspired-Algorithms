import numpy as np

from ._param_grid import ParamGrid
from ._parameter_search_benchmark import ParameterSearchBenchmark
from ._stagnation_stopping_task import StagnationStoppingTask

from NiaPy.algorithms.basic import FireflyAlgorithm

from sklearn.model_selection._search import BaseSearchCV


class NatureInspiredSearchCV(BaseSearchCV):
    __param_grid = None

    def _run_search(self, evaluate_candidates):
        self.__print_run_search_log()

        benchmark = ParameterSearchBenchmark(evaluate_candidates, self.__param_grid)

        task = StagnationStoppingTask(
            length=len(self.__param_grid),
            n_gen=self.__n_gen,
            max_stagnating_gen=self.__max_stagnating_gen,
            benchmark=benchmark
        )

        algorithm = FireflyAlgorithm()
        algorithm.setParameters(NP=40)

        algorithm.run(task=task)

    def __init__(self, estimator, param_grid, max_n_gen=100, max_stagnating_gen=5, scoring=None, n_jobs=None, iid='deprecated', refit=True, cv=None, verbose=0,
                 pre_dispatch='2*n_jobs', error_score=np.nan, return_train_score=True):
        super().__init__(estimator, scoring, n_jobs, iid, refit, cv, verbose, pre_dispatch, error_score,
                         return_train_score)

        self.__n_gen = max_n_gen
        self.__max_stagnating_gen = max_stagnating_gen
        self.__param_grid = ParamGrid(param_grid)

    def __print_run_search_log(self):
        candidates = self.__param_grid.get_number_of_candidates()

        if self.cv is not None:
            print(f'Fitting {self.cv} folds for some of the {candidates} candidates, '
                  f'which might total in {candidates * self.cv} fits')
        else:
            print(f'Fitting at most {candidates} candidates')
