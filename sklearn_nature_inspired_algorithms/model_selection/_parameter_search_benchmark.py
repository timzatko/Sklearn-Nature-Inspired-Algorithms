from NiaPy.benchmarks import Benchmark


class ParameterSearchBenchmark(Benchmark):
    def __init__(self, param_grid, eval_fn):
        self.param_grid = param_grid
        self.eval_fn = eval_fn

        Benchmark.__init__(self, 0, 1)

    def function(self):
        def evaluate(_, solution_vec):
            return self.eval_fn(solution_vec)

        return evaluate
