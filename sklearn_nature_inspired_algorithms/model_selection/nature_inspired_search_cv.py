import numpy as np

from ._param_grid import ParamGrid
from ._parameter_search_benchmark import ParameterSearchBenchmark
from ._stagnation_stopping_task import StagnationStoppingTask

from NiaPy.algorithms.basic import FireflyAlgorithm, BatAlgorithm, GreyWolfOptimizer

from sklearn.model_selection._search import BaseSearchCV

SUPPORTED_ALGORITHMS = ['fa', 'gwo', 'ba']


class NatureInspiredSearchCV(BaseSearchCV):
    __param_grid = None
    __algorithm = None

    def _run_search(self, evaluate_candidates):
        self.__print_run_search_log()

        benchmark = ParameterSearchBenchmark(evaluate_candidates, self.__param_grid)

        task = StagnationStoppingTask(
            length=len(self.__param_grid),
            n_gen=self.__n_gen,
            max_stagnating_gen=self.__max_stagnating_gen,
            benchmark=benchmark
        )

        self.__algorithm.run(task=task)

    def __init__(self, estimator, param_grid, algorithm='fa', population_size=25, max_n_gen=100,
                 max_stagnating_gen=5, scoring=None, n_jobs=None, iid='deprecated', refit=True, cv=None, verbose=0,
                 pre_dispatch='2*n_jobs', error_score=np.nan, return_train_score=True):
        super().__init__(estimator, scoring, n_jobs, iid, refit, cv, verbose, pre_dispatch, error_score,
                         return_train_score)

        self.__n_gen = max_n_gen
        self.__max_stagnating_gen = max_stagnating_gen
        self.__param_grid = ParamGrid(param_grid)
        self.__algorithm = self.__get_algorithm(algorithm, population_size)

    def __print_run_search_log(self):
        candidates = self.__param_grid.get_number_of_candidates()

        if self.cv is not None:
            print(f'Fitting {self.cv} folds for some of the {candidates} candidates, '
                  f'which might total in {candidates * self.cv} fits')
        else:
            print(f'Fitting at most {candidates} candidates')

    @staticmethod
    def __get_algorithm(algorithm, population_size):
        if isinstance(algorithm, str):
            if algorithm not in SUPPORTED_ALGORITHMS:
                raise ValueError(f'"{algorithm}" is not in supported algorithms: {", ".join(SUPPORTED_ALGORITHMS)}')

            algorithm_obj = None

            if algorithm == 'fa':
                algorithm_obj = FireflyAlgorithm()
            elif algorithm == 'ba':
                algorithm_obj = BatAlgorithm()
            elif algorithm == 'gwo':
                algorithm_obj = GreyWolfOptimizer()

            algorithm_obj.setParameters(NP=population_size)

            return algorithm_obj

        return algorithm
