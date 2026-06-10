import unittest

from types import SimpleNamespace

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.axes import Axes

from sklearn_nature_inspired_algorithms.helpers import score_by_generation_lineplot, score_by_generation_violinplot

matplotlib.use('Agg')


class PlotsTestCase(unittest.TestCase):
    def setUp(self):
        # two runs with three generations each and two evaluations per generation,
        # the helpers only read the optimization_logs_ of the search
        self.nia_search = SimpleNamespace(optimization_logs_=[
            [(1, 0.50), (1, 0.55), (2, 0.60), (2, 0.65), (3, 0.70), (3, 0.75)],
            [(1, 0.40), (1, 0.45), (2, 0.55), (2, 0.60), (3, 0.65), (3, 0.70)],
        ])

    def tearDown(self):
        plt.close('all')

    def test_lineplot_returns_axes_for_all_metrics(self):
        for metric in ['min', 'max', 'median', 'mean']:
            ax = score_by_generation_lineplot(self.nia_search, metric=metric)

            self.assertIsInstance(ax, Axes)

            plt.close('all')

    def test_lineplot_with_custom_ax_and_ylim(self):
        _, ax = plt.subplots()

        self.assertIsInstance(score_by_generation_lineplot(self.nia_search, ax=ax, ylim=(0, 1)), Axes)

    def test_lineplot_with_invalid_metric(self):
        with self.assertRaisesRegex(ValueError, 'is not in the allowed metrics'):
            score_by_generation_lineplot(self.nia_search, metric='sum')

    def test_violinplot_returns_axes(self):
        self.assertIsInstance(score_by_generation_violinplot(self.nia_search, run=1), Axes)

    def test_violinplot_with_custom_ax_and_ylim(self):
        _, ax = plt.subplots()

        self.assertIsInstance(score_by_generation_violinplot(self.nia_search, run=0, ax=ax, ylim=(0, 1)), Axes)

    def test_violinplot_with_invalid_run(self):
        with self.assertRaisesRegex(ValueError, 'does not exist'):
            score_by_generation_violinplot(self.nia_search, run=2)


if __name__ == '__main__':
    unittest.main()
