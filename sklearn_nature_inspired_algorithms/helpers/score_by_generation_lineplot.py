import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

ALLOWED_METRICS = ['min', 'max', 'median', 'mean']


def score_by_generation_lineplot(nia_search, metric='max', ax=None, ylim=None):
    if metric not in ALLOWED_METRICS:
        raise ValueError(f'{metric} is not in the allowed metrics! ({ALLOWED_METRICS})')

    optimization_logs_by_runs = []

    for run, optimization_logs in enumerate(nia_search.optimization_logs_):
        for log in optimization_logs:
            optimization_logs_by_runs.append((run, *log))

    df = pd.DataFrame(optimization_logs_by_runs, columns=['run', 'generation', 'score'])

    score_df = df.groupby(['run', 'generation']) \
        .agg({'score': [np.min, np.max, np.mean, np.median]}) \
        .reset_index()

    # remove multilevel columns
    score_df.columns = [[col_ for col_ in col if len(col_)][-1] for col in score_df.columns.values]

    # rename columns with weird names
    score_df = score_df.rename(columns={'amax': 'max', 'amin': 'min'})
    # rename score column
    score_df = score_df.rename(columns={metric: f'{metric} score'})

    if ax is None:
        _, ax = plt.subplots()

    if ylim is not None:
        ax.set(ylim=ylim)

    return sns.lineplot(x="generation", y=f'{metric} score', data=score_df, hue='run')
