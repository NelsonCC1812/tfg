from collections import namedtuple

# misc configs -----------------------------------------------------------------
RANDOM_STATE = None

PRIORIZE = 'f1'
ORDER_BY = 'f1_score'

# data manipulation-------------------------------------------------------------
cv = 5
from sklearn.model_selection import KFold, StratifiedKFold
def folder(): return StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)


# param grids ------------------------------------------------------------------
param_grids = namedtuple('Param_grids', 'logic rfc knn svc')(**{
    "logic": {
        'model__Cs': [[0.01, 0.1, 1, 10, 100]],
        'model__penalty': ['l1', 'l2'],
        'model__solver': ['liblinear'],
        'model__fit_intercept': [True, False],
        'model__max_iter': [100, 200, 300, 400, 500]
    },
    "rfc": {
        'model__n_estimators': [10, 50, 100, 200],
        'model__max_depth': [None, 4, 8, 32, 64],
        'model__min_samples_split': [2, 5, 10],
        'model__min_samples_leaf': [1, 2, 4],
    },
    "knn": {
   	    'model__n_neighbors': [3, 5, 7, 9],
	    'model__weights': ['uniform', 'distance'],
	    'model__metric': ['euclidean', 'manhattan'],
        'model__p': [1, 2]
    },
    "svc": {
        'model__C': [0.1, 1, 10, 100],
        'model__kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'model__gamma': ['scale', 'auto'],
        'model__probability': [True],
    }
})

# scalers ----------------------------------------------------------------------
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scalers = namedtuple('Scalers', 'logic rfc knn svc')(**{
    "logic":    MinMaxScaler(),
    "rfc":      MinMaxScaler(),
    "knn":      MinMaxScaler(),
    "svc":      MinMaxScaler()
})
