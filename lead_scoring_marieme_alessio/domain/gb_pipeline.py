import numpy as np 
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn import svm, datasets

import matplotlib.pyplot as plt
import seaborn as sns

import lead_scoring_marieme_alessio.config.config as cf
from lead_scoring_marieme_alessio.infrastructure.cleanDataTransformer import CleanDataTransformer
from lead_scoring_marieme_alessio.domain.categoricalTransformer import CategoricalTransformer
from lead_scoring_marieme_alessio.domain.numericalTransformer import NumericalTransformer
from lead_scoring_marieme_alessio.domain.featureSelector import FeatureSelector
from lead_scoring_marieme_alessio.domain.evaluate_model import evaluate_model
from  lead_scoring_marieme_alessio.domain.pipeline_transformer import pipeline_transformer



def gb_pipeline(X_train, y_train) :
    
    full_pipeline = pipeline_transformer()

    gb_pipeline = Pipeline( steps = [ 
        ( 'full_pipeline', full_pipeline),
        ( 'gb', GradientBoostingClassifier() ) 
    ])
    gb_pipeline.fit( X_train, y_train )

    return gb_pipeline


























