import unittest

from niapy.problems import Problem

from sklearn_nature_inspired_algorithms.model_selection._stagnation_stopping_task import StagnationStoppingTask


class ConstantProblem(Problem):
    def __init__(self):
        super().__init__(dimension=2, lower=0, upper=1)

    def _evaluate(self, x):
        return 0.0


class StagnationStoppingTaskTestCase(unittest.TestCase):
    def test_max_stagnating_gen_must_be_int_or_none(self):
        with self.assertRaisesRegex(ValueError, 'should be int or None'):
            StagnationStoppingTask(max_iters=10, max_stagnating_gen='5', problem=ConstantProblem())

    def test_max_stagnating_gen_must_be_at_least_one(self):
        with self.assertRaisesRegex(ValueError, 'greater or equal to 1'):
            StagnationStoppingTask(max_iters=10, max_stagnating_gen=0, problem=ConstantProblem())

    def test_stops_when_score_stagnates(self):
        task = StagnationStoppingTask(max_iters=10, max_stagnating_gen=1, problem=ConstantProblem())

        task.x_f = 1.0
        task.eval_stagnation()  # the first generation only sets the baseline score

        self.assertFalse(task.is_stagnating)
        self.assertFalse(task.stopping_condition())

        task.eval_stagnation()  # the score did not improve, the stagnation limit is reached

        self.assertTrue(task.is_stagnating)
        self.assertTrue(task.stopping_condition())


if __name__ == '__main__':
    unittest.main()
