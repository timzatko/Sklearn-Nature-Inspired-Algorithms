from niapy.task import Task, OptimizationType


class StagnationStoppingTask(Task):
    prev_x_f = None

    def __init__(self, max_stagnating_gen=None, iteration_finished_callback=None, **kwargs):
        super().__init__(**kwargs,
                         optimization_type=OptimizationType.MINIMIZATION)

        if not isinstance(max_stagnating_gen, int):
            if max_stagnating_gen is not None:
                raise ValueError('max_stagnating_gen should be int or None!')

        if max_stagnating_gen is not None and max_stagnating_gen < 1:
            raise ValueError('max_stagnating_gen greater or equal to 1!')

        self.max_stagnating_gen = max_stagnating_gen

        # logs array of (generation, score)
        self.optimization_logs_ = []

        self.stagnating_gen_count = 0
        self.stagnating_gen_eval_count = 0
        self.is_stagnating = False
        self.iteration_finished_callback = iteration_finished_callback

    def eval_stagnation(self):
        # the better score is "lower" since the optimization type is "MINIMIZATION"
        if self.prev_x_f is None or self.x_f < self.prev_x_f:
            self.prev_x_f = self.x_f
            self.stagnating_gen_count = 0
        else:
            self.stagnating_gen_count += 1

        if self.stagnating_gen_count >= self.max_stagnating_gen:
            self.is_stagnating = True

    def eval(self, A):
        x_f = super().eval(A)
        self.optimization_logs_.append((self.iters, x_f))
        return x_f

    def stopping_condition(self):
        if self.is_stagnating:
            return True

        return super().stopping_condition()

    def next_iter(self):
        super().next_iter()

        if self.max_stagnating_gen:
            self.eval_stagnation()

            if self.iteration_finished_callback:
                self.iteration_finished_callback(self.iters, self.stagnating_gen_count)
