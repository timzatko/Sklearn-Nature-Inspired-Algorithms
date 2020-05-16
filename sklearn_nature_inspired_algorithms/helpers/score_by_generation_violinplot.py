import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt


def score_by_generation_violinplot(nia_search, **kwargs):
    df = pd.DataFrame(nia_search.optimization_logs_, columns=['generation', 'score'])

    ax = kwargs.get('ax', None)
    ylim = kwargs.get('ylim', (0, 1))

    if ax is None:
        _, ax = plt.subplots()

    ax.set(ylim=ylim)

    return sns.violinplot(x="generation", y="score", data=df)
