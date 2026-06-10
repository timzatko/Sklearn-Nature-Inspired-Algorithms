from abc import ABC

from niapy.problems import Problem


class ParameterSearch(Problem, ABC):
    evaluation_count = 0

    def __init__(self, evaluate_candidates, param_grid):
        self.evaluate_candidates = evaluate_candidates
        self.param_grid = param_grid
        # the algorithms revisit the same candidates, caching the scores
        # avoids repeating the expensive cross-validation
        self.cache = {}

        Problem.__init__(self, dimension=len(param_grid), lower=0, upper=1)

    def get_cached_score(self, cache_key):
        if cache_key in self.cache:
            return self.cache[cache_key]

        return None

    def set_cached_score(self, cache_key, score):
        self.cache[cache_key] = score

    def _evaluate(self, solution_vec):
        # the cache is keyed by the indices of the selected parameter values
        # since the values themselves may not be hashable (e.g. dicts)
        cache_key = self.param_grid.get_value_indices_from_solution_vec(solution_vec)

        score = self.get_cached_score(cache_key)

        if score is None:
            params = self.param_grid.get_params_from_solution_vec(solution_vec)
            cv_results = self.evaluate_candidates([params])
            mean_test_score = cv_results['mean_test_score']
            # we need to invert the score since we are doing
            # a minimization task
            score = -mean_test_score[self.evaluation_count]
            self.evaluation_count += 1
            self.set_cached_score(cache_key, score)

        return score
