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

import src.config.config as cf
from src.infrastructure.CleanDataTransformer import CleanDataTransformer
from src.domain.CategoricalTransformer import CategoricalTransformer
from src.domain.NumericalTransformer import NumericalTransformer
from src.domain.FeatureSelector import FeatureSelector
from src.domain.evaluate_model import evaluate_model
from  src.domain.pipeline_transformer import pipeline_transformer



def rf_pipeline(X_train, y_train):
    
    full_pipeline = pipeline_transformer()


    rf_pipeline = Pipeline( steps = [ 
        ( 'full_pipeline', full_pipeline),
        ( 'rf', RandomForestClassifier() ) 
    ])
    rf_pipeline.fit( X_train, y_train )


    return rf_pipeline


























