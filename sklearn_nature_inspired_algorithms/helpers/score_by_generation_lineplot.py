import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def score_by_generation_lineplot(nia_search, **kwargs):
    metrics = kwargs.get('metrics', ['min', 'max', 'mean', 'median'])

    df = pd.DataFrame(nia_search.optimization_logs_, columns=['generation', 'score'])
    score_df = df.groupby('generation')\
        .agg({'score': [np.min, np.max, np.mean, np.median]})\
        .reset_index()\
        .score\
        .rename(columns={'amax': 'max', 'amin': 'min'})

    data = []

    for metric in score_df.columns:
        for generation, score in enumerate(score_df[metric]):
            data.append((generation, metric, score))

    new_df = pd.DataFrame(data, columns=['generation', 'metric', 'score'])
    new_df = new_df[new_df['metric'].contains(metrics)]

    ax = kwargs.get('ax', None)
    ylim = kwargs.get('ylim', None)

    if ax is None:
        _, ax = plt.subplots()

    if ylim is not None:
        ax.set(ylim=ylim)

    return sns.lineplot(x="generation", y="score", data=new_df, hue='metric')
