from NiaPy.task import StoppingTask, OptimizationType


class StagnationStoppingTask(StoppingTask):
    prev_x_f = None
    stagnation_gen_count = 0

    def __init__(self, max_stagnating_gen=None, **kwargs):
        super().__init__(**kwargs,
                         D=kwargs.get('length'),
                         nGEN=kwargs.get('n_gen'),
                         optType=OptimizationType.MINIMIZATION)

        if not isinstance(max_stagnating_gen, int):
            if max_stagnating_gen is not None:
                raise ValueError('max_stagnating_gen should be int or None!')

        if max_stagnating_gen is not None and max_stagnating_gen < 1:
            raise ValueError('max_stagnating_gen greater or equal to 1!')

        self.max_stagnating_gen = max_stagnating_gen

    def stopCond(self):
        if self.max_stagnating_gen is not None:
            # the better score is "lower" since the optimization type is "MINIMIZATION"
            if self.prev_x_f is None or self.x_f < self.prev_x_f:
                self.prev_x_f = self.x_f
                self.stagnation_gen_count = 0
            else:
                self.stagnation_gen_count += 1

            if self.stagnation_gen_count >= self.max_stagnating_gen:
                return True

        return super().stopCond()
