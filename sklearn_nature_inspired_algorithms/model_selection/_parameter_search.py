from abc import ABC

from niapy.problems import Problem


class ParameterSearch(Problem, ABC):
    evaluation_count = 0

    def __init__(self, evaluate_candidates, param_grid):
        self.evaluate_candidates = evaluate_candidates
        self.param_grid = param_grid
        self.cache = {}

        Problem.__init__(self, dimension=len(param_grid), lower=0, upper=1)

    def get_cache_key(self, params):
        keys = self.param_grid.keys()
        return tuple([params[key] for key in keys])

    def get_cached_score(self, params):
        cache_key = self.get_cache_key(params)

        if cache_key in self.cache:
            return self.cache[cache_key]

        return None

    def set_cached_score(self, params, score):
        cache_key = self.get_cache_key(params)
        self.cache[cache_key] = score

    def _evaluate(self, solution_vec):
        params = self.param_grid.get_params_from_solution_vec(solution_vec)

        score = self.get_cached_score(params)

        if score is None:
            cv_results = self.evaluate_candidates([params])
            mean_test_score = cv_results['mean_test_score']
            # we need to invert the score since we are doing
            # a minimization task
            score = -mean_test_score[self.evaluation_count]
            self.evaluation_count += 1
            self.set_cached_score(params, score)

        return score
