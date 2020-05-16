import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt


def score_by_generation_violinplot(nia_search, run=0, ax=None, ylim=None):
    if run >= len(nia_search.optimization_logs_):
        raise ValueError(f'Specified run ({run}) does not exist!')

    df = pd.DataFrame(nia_search.optimization_logs_[run], columns=['generation', 'score'])

    if ax is None:
        _, ax = plt.subplots()

    if ylim is not None:
        ax.set(ylim=ylim)

    return sns.violinplot(x="generation", y="score", data=df)
