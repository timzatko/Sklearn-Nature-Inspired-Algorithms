import numpy as np

from sklearn.model_selection._search import BaseSearchCV


class NatureInspiredSearchCV(BaseSearchCV):
    def _run_search(self, evaluate_candidates):
        pass

    def __init__(self, estimator, scoring=None, n_jobs=None, iid='deprecated', refit=True, cv=None, verbose=0,
                 pre_dispatch='2*n_jobs', error_score=np.nan, return_train_score=True):
        super().__init__(estimator, scoring, n_jobs, iid, refit, cv, verbose, pre_dispatch, error_score,
                         return_train_score)
