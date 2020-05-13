import unittest

from sklearn_nature_inspired_algorithms.model_selection._param_grid import ParamGrid


class ParamGridTestCase(unittest.TestCase):
    def setUp(self):
        param_grid_value = {
            'param_a': [100],
            'param_b': range(1, 11),
            'param_c': [0.1, 0.2, 0.3, 0.4]
        }

        self.param_grid = ParamGrid(param_grid_value)

    def test_param_grid_index_and_key_mappings(self):
        self.assertEqual(self.param_grid.index_to_key_map, {
            0: 'param_a',
            1: 'param_b',
            2: 'param_c',
        })

        self.assertEqual(self.param_grid.key_to_index_map, {
            'param_a': 0,
            'param_b': 1,
            'param_c': 2,
        })

    def test_get_params_from_solution_vec(self):
        self.assertEqual(
            self.param_grid.get_params_from_solution_vec([0, 1, 0]),
            {
                'param_a': 100,
                'param_b': 10,
                'param_c': 0.1,
            }
        )

        self.assertEqual(
            self.param_grid.get_params_from_solution_vec([0.8, 0.89, 0.24]),
            {
                'param_a': 100,
                'param_b': 9,
                'param_c': 0.1,
            }
        )

        self.assertEqual(
            self.param_grid.get_params_from_solution_vec([0.8, 0.9, 0.25]),
            {
                'param_a': 100,
                'param_b': 10,
                'param_c': 0.2,
            }
        )

        self.assertEqual(
            self.param_grid.get_params_from_solution_vec([0.8, 0.5, 0.8]),
            {
                'param_a': 100,
                'param_b': 6,
                'param_c': 0.4,
            }
        )


if __name__ == '__main__':
    unittest.main()
