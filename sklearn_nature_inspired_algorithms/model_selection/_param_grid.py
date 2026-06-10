import math
import numpy as np


class ParamGrid:
    def __init__(self, param_grid):
        self.param_grid = param_grid

        self.key_to_index_map = {}
        self.index_to_key_map = {}

        self.__keys = []

        if param_grid is None:
            raise ValueError('param_grid cannot be None!')

        param_grid_key_indices = tuple(param_grid.keys())

        for index, key in enumerate(param_grid_key_indices):
            self.__keys.append(key)
            self.key_to_index_map[key] = index
            self.index_to_key_map[index] = key

    def __len__(self):
        return len(self.param_grid)

    def keys(self):
        return tuple(self.__keys)

    def values(self):
        return self.param_grid.values()

    def get_number_of_candidates(self):
        return np.multiply.reduce([len(value) for value in self.param_grid.values()])

    def get_params_from_solution_vec(self, solution_vec):
        params = {}

        for param_key in self.param_grid:
            params[param_key] = self.__get_param_value(param_key, solution_vec)

        return params

    def get_value_indices_from_solution_vec(self, solution_vec):
        # the tuple of selected value indices uniquely identifies a candidate,
        # and unlike the values themselves, it is always hashable
        return tuple(self.__get_param_value_index(param_key, solution_vec) for param_key in self.param_grid)

    def __get_param_value(self, param_key, solution_vec):
        param_value_index = self.__get_param_value_index(param_key, solution_vec)
        return self.param_grid[param_key][param_value_index]

    def __get_param_value_index(self, param_key, solution_vec):
        index = self.key_to_index_map[param_key]
        solution_value = solution_vec[index]
        param_value_count = len(self.param_grid[param_key])
        # the solution value is from the [0, 1] interval, split it into equally
        # sized buckets, one for each of the parameter values, min() handles
        # the edge case when the solution value is exactly 1
        return min(math.floor(solution_value / (1 / param_value_count)), param_value_count - 1)
